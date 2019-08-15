{
    "targets": [
        {
            "target_name": "cryptonight-hashing",
            "sources": [
                '<!@(uname -a | grep "x86_64" >/dev/null && echo "xmrig/crypto/cn/asm/cn_main_loop.S" || echo)',
                '<!@(uname -a | grep "x86_64" >/dev/null && echo "xmrig/crypto/cn/asm/CryptonightR_template.S" || echo)',
                '<!@(uname -a | grep "x86_64" >/dev/null && echo "xmrig/crypto/cn/r/CryptonightR_gen.cpp" || echo)',
                '<!@(uname -a | grep "x86_64" >/dev/null && (grep avx2 /proc/cpuinfo >/dev/null && echo "xmrig/crypto/cn/gpu/cn_gpu_avx.cpp" || echo) || echo)',
                '<!@(uname -a | grep "x86_64" >/dev/null && echo "xmrig/crypto/cn/gpu/cn_gpu_ssse3.cpp" || echo)',
                '<!@(uname -a | grep "x86_64" >/dev/null || echo "xmrig/crypto/cn/gpu/cn_gpu_arm.cpp" || echo)',
                "multihashing.cc",
                "xmrig/crypto/cn/c_blake256.c",
                "xmrig/crypto/cn/c_groestl.c",
                "xmrig/crypto/cn/c_jh.c",
                "xmrig/crypto/cn/c_skein.c",
                "xmrig/crypto/common/keccak.cpp",
                "xmrig-override/crypto/common/Algorithm.cpp",
                "xmrig/crypto/cn/CnCtx.cpp",
                "xmrig/crypto/cn/CnHash.cpp",
                "xmrig/crypto/common/VirtualMemory_unix.cpp",

                "xmrig/crypto/randomx/aes_hash.cpp",
                "xmrig/crypto/randomx/argon2_ref.c",
                "xmrig/crypto/randomx/bytecode_machine.cpp",
                "xmrig/crypto/randomx/dataset.cpp",
                "xmrig/crypto/randomx/soft_aes.cpp",
                "xmrig/crypto/randomx/virtual_memory.cpp",
                "xmrig/crypto/randomx/vm_interpreted.cpp",
                "xmrig/crypto/randomx/allocator.cpp",
                "xmrig/crypto/randomx/randomx.cpp",
                "xmrig/crypto/randomx/superscalar.cpp",
                "xmrig/crypto/randomx/vm_compiled.cpp",
                "xmrig/crypto/randomx/vm_interpreted_light.cpp",
                "xmrig/crypto/randomx/argon2_core.c",
                "xmrig/crypto/randomx/blake2_generator.cpp",
                "xmrig/crypto/randomx/instructions_portable.cpp",
                "xmrig/crypto/randomx/reciprocal.c",
                "xmrig/crypto/randomx/virtual_machine.cpp",
                "xmrig/crypto/randomx/vm_compiled_light.cpp",
                "xmrig/crypto/randomx/blake2/blake2b.c",
                '<!@(uname -a | grep "x86_64" >/dev/null && echo "xmrig/crypto/randomx/jit_compiler_x86_static.S" || echo)',
                '<!@(uname -a | grep "x86_64" >/dev/null && echo "xmrig/crypto/randomx/jit_compiler_x86.cpp" || echo)',

                "xmrig/crypto/defyx/defyx.cpp",
                "xmrig/crypto/defyx/KangarooTwelve.c",
                "xmrig/crypto/defyx/yescrypt-best.c",
            ],
            "include_dirs": [
                "xmrig-override",
                "xmrig",
                "<!(node -e \"require('nan')\")"
            ],
            "cflags_c": [
                '<!@(uname -a | grep "aarch64" >/dev/null && echo "-march=armv8-a+crypto -flax-vector-conversions -DXMRIG_ARM=1" || (uname -a | grep "armv7" >/dev/null && echo "-mfpu=neon -flax-vector-conversions -DXMRIG_ARM=1" || echo "-march=native"))',
                '<!@(grep Intel /proc/cpuinfo >/dev/null && echo -DCPU_INTEL || (grep AMD /proc/cpuinfo >/dev/null && (test `awk \'/cpu family/ && $NF~/^[0-9]*$/ {print $NF}\' /proc/cpuinfo | head -n1` -ge 23 && echo -DAMD || echo -DAMD_OLD) || echo))>',
                "-std=gnu11      -fPIC -DNDEBUG -Ofast -fno-fast-math -w"
            ],
            "cflags_cc": [
                '<!@(uname -a | grep "aarch64" >/dev/null && echo "-march=armv8-a+crypto -flax-vector-conversions -DXMRIG_ARM=1" || (uname -a | grep "armv7" >/dev/null && echo "-mfpu=neon -flax-vector-conversions -DXMRIG_ARM=1" || echo "-march=native"))',
                '<!@(grep Intel /proc/cpuinfo >/dev/null && echo -DCPU_INTEL || (grep AMD /proc/cpuinfo >/dev/null && (test `awk \'/cpu family/ && $NF~/^[0-9]*$/ {print $NF}\' /proc/cpuinfo | head -n1` -ge 23 && echo -DAMD || echo -DAMD_OLD) || echo))>',
                "-std=gnu++11 -s -fPIC -DNDEBUG -Ofast -fno-fast-math -fexceptions -fno-rtti -Wno-class-memaccess -w"
            ]
        }
    ]
}
