import kwikset

kwikset.setup_serial()

kwikset.setup_arduinobreakout_pins()

lock = raw_input("What do you want to do? ")

if(lock == "lock"):
    kwikset.lock()
else:
    kwikset.unlock()