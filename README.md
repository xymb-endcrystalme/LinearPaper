# LinearPaper - Paper that uses Linear region file format

Linear region file format uses about half of the original Anvil region file without any loss of data.

Check [this repository for documentation and tools](https://github.com/xymb-endcrystalme/LinearRegionFileFormatTools).



This fork is 100% compatible with Paper, it just reads and saves region files in `.linear` instead of `.mca`.

Great for giant (TB+) worlds. Offers no advantages for tiny worlds, it's just a region file format.

## Compiling

```
./gradlew applyPatches
./gradlew createReobfPaperclipJar
```

Your compiled .jar will be in `build/libs/`.
