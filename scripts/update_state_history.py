import sys, os, sim, csv
class UpdateStateHistory:
    def setup(self, args):
        self.calling_interval_ns = 100000
        sim.util.Every(self.calling_interval_ns * sim.util.Time.NS, self.periodic, roi_only = True)
        self.num_cores = sim.config.ncores
    def periodic(self, time, time_delta):
        # Don't do anythin on the first call 
        if time_delta == 0:
          return
        for i in range(0, self.num_cores):
             actual_state = sim.dvfs.get_core_state(i) == 5
             sim.dvfs.update_history(i, actual_state)
             sim.dvfs.update_weights(i, actual_state)

sim.util.register(UpdateStateHistory())
