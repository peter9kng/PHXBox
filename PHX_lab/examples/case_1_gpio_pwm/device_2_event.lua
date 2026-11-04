-- version 0.1

if event.type == EVENT_FROM_OTHER_DEVICE then  -- TLS event
    if event.from == 'gateway' and event.topic == 'button pressed' then
        pwm_fade(0, 100, 2000)                      -- turn on LED
        run_later(2000, 'pwm_fade(0, 0, 2000)')     -- turn off LED 2s later
    end
end