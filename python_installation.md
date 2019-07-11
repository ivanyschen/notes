# Python Installation (Using 3.7 for exmple)

*  Install packages needed

   ```bash
   sudo apt update
   ```

   ```bash
   sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev wget
   ```

*  Download desire release's source code from [here](https://www.python.org/downloads/source/):

   ```bash
   curl -O https://www.python.org/ftp/python/3.7.3/Python-3.7.3.tar.xz
   ```

*  Extract

   ```bash
   tar -xf Python-3.7.3.tar.xz
   ```

*  Nevigate to the python source directory and run the `configure` script that will perform a number of checks to make sure all the dependencies on your system are present:

   ```bash
   cd Python-3.7.3
   ```

   ```bash
   ./configure --enable-optimizations
   ```

   Note: `--enable-optimizations` option will optimize the Python binary by running multiple tests which will make the build preocess slower.

*  Run `make` to start the build process:

   ```bash
   make -j 8
   ```

   Note: For faster build time, modify the `-j` flag according to your processor. To figure otu the numbef for the cores, you can find it with `nproc` command. The code snippet above is for machines with 8 cores.

*  After the build is done, install the Python binaries by running the following:

   ```bash
   sudo make altinstall
   ```

   Note: Avoid using `make install`as it'll overwrite the default system `python3` binary.

*  To verify that the Python has been installed successfully, run:

   ```bash
   python3.7 --version
   ```

*  Update python3.7 to update alternatives:

   ```bash
   sudo update-alternatives --install /usr/local/bin/python3 python3 /usr/bin/python3.7 1
   ```

*  Update `python3` to opint to python3.7:

   ```bash
   sudo update-alternatives --config python3
   ```

Original sources:

[1] [https://linuxize.com/post/how-to-install-python-3-7-on-debian-9/](https://linuxize.com/post/how-to-install-python-3-7-on-debian-9/)

[2] [https://jcutrer.com/linux/upgrade-python37-ubuntu1810](https://jcutrer.com/linux/upgrade-python37-ubuntu1810)

