import hbp_nrp_cle.tf_framework as nrp

nrp.config.brain_root.red_connection
nrp.config.brain_root.red_connection_1
nrp.config.brain_root.red_connection_2
nrp.config.brain_root.red_connection_3
nrp.config.brain_root.red_connection_4
nrp.config.brain_root.blue_connection
nrp.config.brain_root.blue_connection_1
nrp.config.brain_root.blue_connection_2
nrp.config.brain_root.blue_connection_3
nrp.config.brain_root.blue_connection_4
@nrp.Robot2Neuron()
def csv_weights_monitor (t):
    clientLogger.info("Angular_Red", nrp.config.brain_root.red_connection.get("weight",format="list"))
    clientLogger.info("Angular_Red_1", nrp.config.brain_root.red_connection_1.get("weight",format="list"))
    clientLogger.info("Angular_Red_2", nrp.config.brain_root.red_connection_2.get("weight",format="list"))
    clientLogger.info("Angular_Red_3", nrp.config.brain_root.red_connection_3.get("weight",format="list"))
    clientLogger.info("Angular_Red_4", nrp.config.brain_root.red_connection_4.get("weight",format="list"))
    clientLogger.info("Angular_blue", nrp.config.brain_root.blue_connection.get("weight",format="list"))
    clientLogger.info("Angular_blue_1", nrp.config.brain_root.blue_connection_1.get("weight",format="list"))
    clientLogger.info("Angular_blue_2", nrp.config.brain_root.blue_connection_2.get("weight",format="list"))
    clientLogger.info("Angular_blue_3", nrp.config.brain_root.blue_connection_3.get("weight",format="list"))
    clientLogger.info("Angular_blue_4", nrp.config.brain_root.blue_connection_4.get("weight",format="list"))