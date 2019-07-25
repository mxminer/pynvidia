# pynvidia
a python library for manipulating nvidia Graphic cards using nvidia-smi/nvidia-settings

gpuinfo生成后为一个list嵌套的{} 中间某些元素的item为OrderedDict 


product_name P104-100

product_brand GeForce

accounting_mode_buffer_size 4000

uuid GPU-22ac5d6b-6ba4-550d-5348-0aa3758f0a57

minor_number 2

fan_speed 32 %

fb_memory_usage OrderedDict([('total', '4042 MiB'), ('used', '0 MiB'), ('free', '4042 MiB')])

temperature OrderedDict([('gpu_temp', '39 C'), ('gpu_temp_max_threshold', '96 C'), ('gpu_temp_slow_threshold', '93 C'), ('gpu_temp_max_gpu_threshold', 'N/A'), ('memory_temp', 'N/A'), ('gpu_temp_max_mem_threshold', 'N/A')])

power_readings OrderedDict([('power_state', 'P8'), ('power_management', 'Supported'), ('power_draw', '7.32 W'), ('power_limit', '180.00 W'), ('default_power_limit', '180.00 W'), ('enforced_power_limit', '180.00 W'), ('min_power_limit', '90.00 W'), ('max_power_limit', '217.00 W')])

clocks OrderedDict([('graphics_clock', '139 MHz'), ('sm_clock', '139 MHz'), ('mem_clock', '405 MHz'), ('video_clock', '544 MHz')])

max_clocks OrderedDict([('graphics_clock', '1911 MHz'), ('sm_clock', '1911 MHz'), ('mem_clock', '5005 MHz'), ('video_clock', '1708 MHz')])
