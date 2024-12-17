import speedtest

test = speedtest.Speedtest()

download = test.download() / 1_000_000
  
upload = test.upload() / 1_000_000     

print(f"Download Speed: {download:.2f} Mbps")
print(f"Upload Speed: {upload:.2f} Mbps")
