import pynvml


def get_gpu_properties():
    pynvml.nvmlInit()
    device_count = pynvml.nvmlDeviceGetCount()

    for i in range(device_count):
        handle = pynvml.nvmlDeviceGetHandleByIndex(i)
        name = pynvml.nvmlDeviceGetName(handle).decode('utf-8')
        print("GPU Device {}: {}".format(i, name))

        compute_capability = pynvml.nvmlDeviceGetCudaComputeCapability(handle)
        multiprocessor_count = pynvml.nvmlDeviceGetAttribute(
            handle, pynvml.NVML_DEVICE_ATTRIBUTE_MULTIPROCESSOR_COUNT)
        clock_rate = pynvml.nvmlDeviceGetClockInfo(
            handle, pynvml.NVML_CLOCK_SM)
        memory_info = pynvml.nvmlDeviceGetMemoryInfo(handle)
        memory_capacity = memory_info.total / \
            (1024 * 1024 * 1024)  # Convert to GB
        teraflops = (compute_capability[0] * 100 + compute_capability[1]
                     * 10) / 2 * multiprocessor_count * (clock_rate / 1000000) * 2
        print("  Compute Capability: {}.{}".format(
            compute_capability[0], compute_capability[1]))
        print("  Multiprocessors: {}".format(multiprocessor_count))
        print("  Clock Rate: {:.2f} GHz".format(clock_rate / 1000000))
        print("  Memory Capacity: {:.2f} GB".format(memory_capacity))
        print("  Teraflops: {:.2f} TFLOPS".format(teraflops))


if __name__ == "__main__":
    get_gpu_properties()
