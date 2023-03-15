# scripts
Useful scripts for repetitive or detailed processes

## encode_converter.py
Copia e converter arquivos de uma pasta e subpastas especificada, para um ENCODE válido especificado.
This conversion will only be performed on files with `.pas` and `.dfm` extensions, but this can easily be changed in code.

``` shell
python encode_converter.py <source_path> <target_path> <target_encode>
```
- `<source_path>` Folder of original files for conversion
- `<target_path>` Destination folder for converted files
- `<target_encode>` Conversion target encode name

> You can find a list of valid encodes at [chardet library documentation](https://github.com/chardet/chardet).
