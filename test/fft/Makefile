TARGET=fft
include ../shared/Makefile.shared

$(TARGET): $(TARGET).o
	$(CC) $(TARGET).o -lm $(SNIPER_LDFLAGS) -o $(TARGET)

run_$(TARGET):
	../../run-sniper -v -s update_state_history -n 8 -c gainestown --roi --power -- ./fft -p 8

CLEAN_EXTRA=viz
