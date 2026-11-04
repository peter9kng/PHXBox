-- ver 0.1

if event.type == EVENT_GPIO then         -- gpio event
    if event.gpio_event.pin == 21 and event.gpio_event.value == 1 then
        send_event('device_2', 'button pressed', {btn=1})
    end
end


