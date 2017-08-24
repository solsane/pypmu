from synchrophasor.pmu import Pmu
from synchrophasor.frame import ConfigFrame2
from synchrophasor.file import DataFile

"""
tinyPMU will listen on ip:port for incoming connections.
When tinyPMU receives command to start sending
measurements - fixed (sample) measurement will
be sent.
"""


if __name__ == "__main__":
##TODO: support for non-multistreaming here. Also, replace hard coding with actual values from file.



    station_names =  ["Station A", "Station B", "Station C", "Station D", "Station E", "Station F", "Station G", "Station H", "Station I", "Station J",
                                                           "Station K", "Station L", "Station M", "Station N"]
    phasor_ids = [1]*14
    data_format = [(True, True, True, True)] * 14

    channel_names = [["aname!"]] * 14
    ph_units = [[(915527, "v")]] * 14

    an_units = [[]]*14
    dig_units = [[]]*14
    fnom = [60]*14
    cfgcount = [1]*14

    cfg = ConfigFrame2(7734, 1000000, 14, station_names, phasor_ids, data_format,
                                          phasor_ids, [0]*14, [0]*14,
                                         channel_names,
                                         ph_units,
                                         an_units,
                                         dig_units, fnom, cfgcount, 30)


    pmu_list = Pmu.split_pmu(cfg)
    print("pmu list", pmu_list)

    print("PMU list done")

    data_file = DataFile(pmu_list,"ieee14_vsc_wtg_out.dat", "ieee14_vsc_wtg_out.lst")

    for pmu in pmu_list:
        pmu.run()

    while True:
        if pmu_list[0].clients:  # Check if there is any connected PDCs
            data_file.run()
            break

    pmu.join()
