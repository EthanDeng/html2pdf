# Convert2Read 轻阅转换器

Convert2Read is a light tool designed to convert html page to standard markdown file, and then convert markdown file to LaTeX file. then process the LaTeX file to PDF using TeX Live or TinyTeX.

Convert2Read 是一个轻型的工具，用于将网页转为标准 Markdown 文件，然后把 Markdown 文件转为 LaTeX 文档，最后借助于 TeX Live 套装或者 TinyTeX 将其编译为一个适合阅读的 PDF 文档。

## Workflow 转换流程

### html -> markdown
目前已有的轮子 tomd 包。

### markdown -> tex
目前考虑手动转为标准的 LaTeX 格式。

### tex -> pdf
暂时先考虑 ctexart 作为模板，后期可能考虑将 ElegantLaTeX 系列模板放进去，或者新建一个简化格式的模板/设置。

## Framework 框架
整体框架使用 Python 内置 tkinter 包进行 GUI 的设计，然后通过 pyinstaller 打包成可执行文件。可能的依赖条件是

+ MikTeX\TeX Live\TinyTeX 三选一；
+ Python。

## Credits

The icon of EZRead Program is made by [Freepik](https://www.flaticon.com/authors/payungkead) from [www.flaticon.com](https://www.flaticon.com).

EZRead 的图标由 [www.flaticon.com](https://www.flaticon.com) 网站的 [Freepik](https://www.flaticon.com/authors/payungkead) 设计制作。

