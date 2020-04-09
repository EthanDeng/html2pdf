import re

f = open('input.md', 'r', encoding='utf-8')
file_string = f.read()
print(file_string)

default_string1 = r"""
\documentclass[cn]{elegantpaper}

\title{Example of Converting Markdown to \LaTeX{} File \\ Markdown 转为 \LaTeX{} 示例}

\author{邓 东 升}
\date{\today}
\usepackage[nodisplayskipstretch]{setspace}
\usepackage{minted}
\usepackage{mdframed}
\usepackage{xcolor}
\definecolor{fpp2}{RGB}{59, 85, 110}
\definecolor{egray}{RGB}{51, 51, 51}
\definecolor{mgray}{RGB}{243, 243, 243}
\BeforeBeginEnvironment{minted}{\begin{mdframed}[backgroundcolor=mgray,hidealllines=true,innertopmargin=-5pt,innerbottommargin=8pt]}
\AfterEndEnvironment{minted}{\end{mdframed}}
% \setminted{bgcolor=mgray}
% \makeatletter
% \patchcmd{\minted@colorbg}{\noindent}{\medskip\noindent}{}{}
% \apptocmd{\endminted@colorbg}{\par\medskip}{}{}
% \makeatother
\AtBeginEnvironment{minted}{
	\setlength{\parskip}{0pt}
	\singlespacing
	}
\usepackage{ulem}

\begin{document}

\maketitle
"""

default_string2 = r"""
\end{document}
"""

# converter = Markdown2LaTeXConverter()
string = re.sub(r'^#{1}\s*([^#].*)$', '\u005c\u005csection{\\1}', file_string, flags=re.MULTILINE)
string = re.sub(r'^#{2}\s*([^#].*)$', '\u005c\u005csubsection{\\1}', string, flags=re.MULTILINE)
string = re.sub(r'(?s)```([a-z]+?)\s(.*?)\s```', '\u005c\u005cbegin{minted}{\\1}\n\\2\n\u005c\u005cend{minted}', string, flags=re.MULTILINE)
string = re.sub(r'(?s)```([a-z]*?)\s(.*?)\s```', '\u005c\u005cbegin{minted}{tex}\n\\2\n\u005c\u005cend{minted}', string, flags=re.MULTILINE)
string = re.sub(r'\*\*([\s\S]*?)\*\*', '\u005c\u005ctextbf{\\1}', string, flags=re.MULTILINE)
string = re.sub(r'\_\_([\s\S]*?)\_\_', '\u005c\u005ctextbf{\\1}', string, flags=re.MULTILINE)
string = re.sub(r'\*([\s\S]*?)\*', '\u005c\u005ctextit{\\1}', string, flags=re.MULTILINE)
string = re.sub(r'\*([\s\S]*?)\*', '\u005c\u005ctextit{\\1}', string, flags=re.MULTILINE)
string = re.sub('[^!]\[(.*?)\]\((.*?)\)', ' \u005c\u005chref{\\2}{\\1}', string,flags=re.MULTILINE)
string = re.sub('!\[(.*?)\]\((.*?)\)', '\u005c\u005cbegin{figure}[htbp]\n\u005c\u005ccentering\n\u005c\u005cincludegraphics[width=0.7\u005c\u005ctextwidth]{\\2}\n\u005c\u005ccaption{\\1}\n\u005c\u005cend{figure}', string, flags=re.MULTILINE)
string = re.sub('>\s([\s\S].*?)\n', '\u005c\u005cbegin{quote}\n\\1\n\u005c\u005cend{quote}\n', string, flags=re.MULTILINE)
string = re.sub('^\s*$\s[0-9]+\.(.*?)\n', '\n\u005c\u005cbegin{enumerate}\n  \u005c\u005citem\\1\n', string, flags=re.MULTILINE)
string = re.sub('^[0-9]+\.(.*?)[\s\S]^\s*$', '  \u005c\u005citem\\1\n\u005c\u005cend{enumerate}\n', string, flags=re.MULTILINE)
string = re.sub('^[0-9]+\.(.*?)\n', '  \u005c\u005citem\\1\n', string, flags=re.MULTILINE)
string = re.sub('^\s*$\s(\-|\+)(.*?)\n', '\n\u005c\u005cbegin{itemize}\n  \u005c\u005citem\\2\n', string, flags=re.MULTILINE)
string = re.sub('^(-|\+)(.*?)[\s\S]^\s*$', '  \u005c\u005citem\\2\n\u005c\u005cend{itemize}\n', string, flags=re.MULTILINE)
string = re.sub('^(-|\+)(.*?)\n', '  \u005c\u005citem\\2\n', string, flags=re.MULTILINE)
string = re.sub('`([^`]*.*?[^`]*)`', '\u005c\u005cmintinline{tex}{\\1}', string, flags=re.MULTILINE)

full_tex_string = default_string1 + '\n' + string + '\n' + default_string2
print(full_tex_string)

output_file = open("output.tex","w+",encoding='utf-8')
for line in full_tex_string:
    output_file.write(line)

output_file.close()
# https://www.reddit.com/r/learnpython/comments/6m0k3x/regex_for_markdown_to_html/djza3zj/
# https://stackoverflow.com/questions/150033/regular-expression-to-match-non-ascii-characters