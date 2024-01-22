## Splitting Large Files

If you have a large file that you need to split into smaller chunks, you can use the `split` command in Linux. For example, to split a file into 1GB chunks:

```bash
split -b 1G -d Rees46.zip Rees46_part_
```

This command will create several files (depending on the size of the original file), each 1GB in size, with names like `Rees46_part_00`, `Rees46_part_01`, etc.

## Reconstructing the Original File

When you need to reconstruct the original file, you can use the `cat` command:

```bash
cat Rees46_part_* > Rees46.zip
```

This command concatenates the parts together into a new zip file. The order of concatenation is determined by the shell (which usually sorts the arguments lexicographically), so it's important to ensure that the parts are correctly numbered.