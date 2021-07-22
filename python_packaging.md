- Python created the Wheel, a package format designed to ship libraries with compiled artifacts. In fact, Python’s package installer, pip, always prefers wheels because installation is always faster, so even pure-Python packages work better with wheels.

- Default to publishing both sdist and wheel archives together, unless you’re creating artifacts for a very specific use case where you know the recipient only needs one or the other.

- Source distributions also contain a bundle of metadata sitting in a directory called <package-name>.egg-info. This metadata helps with building and installing the package, but user’s don’t really need to do anything with it.
