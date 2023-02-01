# tayga

TAYGA is an out-of-kernel stateless NAT64 implementation for Linux.  It uses
the TUN driver to exchange packets with the kernel, which is the same driver
used by OpenVPN and QEMU/KVM.  TAYGA needs no kernel patches or out-of-tree
modules, and it is compatible with all 2.4 and 2.6 kernels.

http://www.litech.org/tayga/
