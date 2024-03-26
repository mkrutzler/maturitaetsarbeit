if grub-file --is-x86-multiboot build/bin/os.bin; then
  echo multiboot confirmed
else
  echo the file is not multiboot
fi
