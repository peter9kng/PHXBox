-- version 0.1

temp, hum = hw_read_sht3x(HW_SHT30)
mqtt_publish("PHX_lab/case2", to_json({temp=temp, hum=hum}))
