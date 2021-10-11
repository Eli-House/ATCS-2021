mount = { "Mount Everest": "29,029", "K2": "28,251", "Kangchenjunga": "28,169", "Lhotse": "27,940", "Makalu": "27,838" }

for name in mount.keys():
    print(name)
for height in mount.values():
    print(height)
for mount, height in mount.items():
    print(mount, "is", height, "feet tall")