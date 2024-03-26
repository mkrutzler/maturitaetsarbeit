
.PHONY: all clean run usb-write build objs iso setup

# Specifying relevant directories and files
SRC_DIR := src
BUILD_DIR := build
TOOLS_DIR := tools
CONFIG_DIR := config

CC := i686-elf-g++
AS := i686-elf-as

DEF_FLAGS := -ffreestanding -O2
EXTRA_FLAGS := -Wall -Wextra -fno-exceptions -fno-rtti

all: setup iso run

setup: clean
	mkdir $(BUILD_DIR)
	mkdir $(BUILD_DIR)/bin
	mkdir $(BUILD_DIR)/iso
	mkdir $(BUILD_DIR)/iso/boot
	mkdir $(BUILD_DIR)/iso/boot/grub

iso: build
	cp $(BUILD_DIR)/bin/os.bin $(BUILD_DIR)/iso/boot/os.bin
	cp $(CONFIG_DIR)/grub.cfg $(BUILD_DIR)/iso/boot/grub/grub.cfg
	grub-mkrescue -o $(BUILD_DIR)/bin/os.iso $(BUILD_DIR)/iso


build: objs
	$(CC) -T $(SRC_DIR)/linker.ld -o $(BUILD_DIR)/bin/os.bin $(DEF_FLAGS) -nostdlib $(BUILD_DIR)/boot.o $(BUILD_DIR)/kernel.o -lgcc
	echo "======== TESTING MULTIBOOT ========"
	sh $(TOOLS_DIR)/testmultiboot.sh


objs:
	$(CC) -c $(SRC_DIR)/kernel.cpp -o $(BUILD_DIR)/kernel.o $(DEF_FLAGS) $(EXTRA_FLAGS)
	$(AS) -c $(SRC_DIR)/boot.s -o $(BUILD_DIR)/boot.o

run: 
	qemu-system-i386 -cdrom $(BUILD_DIR)/bin/os.iso

clean:
	rm -rf build

usb-write: all
	echo "WARNING: THIS WILL ERASE /dev/sdb!!!!"
	read -p "Press Enter to Continue"
	sudo dd if=$(BUILD_DIR)/bin/os.iso of=/dev/sdb && sync
