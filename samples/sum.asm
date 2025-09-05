	.file	"sum.c"
	.intel_syntax noprefix
# GNU C17 (Ubuntu 11.4.0-1ubuntu1~22.04) version 11.4.0 (x86_64-linux-gnu)
#	compiled by GNU C version 11.4.0, GMP version 6.2.1, MPFR version 4.1.0, MPC version 1.2.1, isl version isl-0.24-GMP

# GGC heuristics: --param ggc-min-expand=100 --param ggc-min-heapsize=131072
# options passed: -masm=intel -mtune=generic -march=x86-64 -O0 -fno-omit-frame-pointer -fasynchronous-unwind-tables -fstack-protector-strong -fstack-clash-protection -fcf-protection
	.text
	.section	.rodata
.LC0:
	.string	"%d + %d = %d\n"
	.text
	.globl	main
	.type	main, @function
main:
.LFB0:
	.cfi_startproc
	endbr64	
	push	rbp	#
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	mov	rbp, rsp	#,
	.cfi_def_cfa_register 6
	sub	rsp, 16	#,
# sum.c:6:     a = 10;
	mov	DWORD PTR -12[rbp], 10	# a,
# sum.c:7:     b = 20;
	mov	DWORD PTR -8[rbp], 20	# b,
# sum.c:8:     sum = a + b;
	mov	edx, DWORD PTR -12[rbp]	# tmp88, a
	mov	eax, DWORD PTR -8[rbp]	# tmp89, b
	add	eax, edx	# tmp87, tmp88
	mov	DWORD PTR -4[rbp], eax	# sum, tmp87
# sum.c:10:     printf("%d + %d = %d\n", a, b, sum);
	mov	ecx, DWORD PTR -4[rbp]	# tmp90, sum
	mov	edx, DWORD PTR -8[rbp]	# tmp91, b
	mov	eax, DWORD PTR -12[rbp]	# tmp92, a
	mov	esi, eax	#, tmp92
	lea	rax, .LC0[rip]	# tmp93,
	mov	rdi, rax	#, tmp93
	mov	eax, 0	#,
	call	printf@PLT	#
# sum.c:12:     return 0;
	mov	eax, 0	# _6,
# sum.c:13: }
	leave	
	.cfi_def_cfa 7, 8
	ret	
	.cfi_endproc
.LFE0:
	.size	main, .-main
	.ident	"GCC: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0"
	.section	.note.GNU-stack,"",@progbits
	.section	.note.gnu.property,"a"
	.align 8
	.long	1f - 0f
	.long	4f - 1f
	.long	5
0:
	.string	"GNU"
1:
	.align 8
	.long	0xc0000002
	.long	3f - 2f
2:
	.long	0x3
3:
	.align 8
4:
