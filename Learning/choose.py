@nrp.MapSpikeSink("linear_red", nrp.brain.linear_sensor[0:1], nrp.spike_recorder)
@nrp.MapSpikeSink("linear_blu", nrp.brain.linear_sensor[1:2], nrp.spike_recorder)
@nrp.MapSpikeSink("linear_yellow", nrp.brain.linear_sensor[2:3], nrp.spike_recorder)
@nrp.MapSpikeSink("linear_cyan", nrp.brain.linear_sensor[3:4], nrp.spike_recorder)
@nrp.MapSpikeSink("linear_black", nrp.brain.linear_sensor[4:5], nrp.spike_recorder)
@nrp.MapSpikeSink("feedback", nrp.brain.feedback, nrp.spike_recorder)
@nrp.MapSpikeSink("error", nrp.brain.error_neuron[0:1], nrp.spike_recorder)
@nrp.MapSpikeSink("error_2", nrp.brain.error_neuron[1:2], nrp.spike_recorder)
@nrp.MapVariable("blue_dir",initial_value = 0, scope = nrp.GLOBAL)
@nrp.MapVariable("red_dir",initial_value = 0, scope = nrp.GLOBAL)
@nrp.MapVariable("yellow_dir",initial_value = 0, scope = nrp.GLOBAL)
@nrp.MapVariable("cyan_dir",initial_value = 0, scope = nrp.GLOBAL)
@nrp.MapVariable("black_dir",initial_value = 0, scope = nrp.GLOBAL)
@nrp.MapVariable("turn_f",initial_value = 0, scope = nrp.GLOBAL)
@nrp.MapVariable("turn_bis",initial_value = 0, scope = nrp.GLOBAL)
@nrp.MapVariable("turn_ter",initial_value = 0, scope = nrp.GLOBAL)
@nrp.MapVariable("choice", initial_value = 0, scope = nrp.GLOBAL)
@nrp.MapVariable("start_choice", initial_value = 0, scope = nrp.GLOBAL)
@nrp.MapVariable("flag", initial_value = 0, scope = nrp.GLOBAL)
@nrp.MapVariable("err", initial_value = 0, scope = nrp.GLOBAL)
@nrp.MapVariable("err_1", initial_value = 0, scope = nrp.GLOBAL)
@nrp.MapVariable("err_2", initial_value = 0, scope = nrp.GLOBAL)
@nrp.MapVariable("err_3", initial_value = 0, scope = nrp.GLOBAL)
@nrp.MapVariable("second_obj",initial_value = 0,scope = nrp.GLOBAL)
@nrp.Robot2Neuron()
def choose (t,linear_red,linear_blu,linear_yellow,linear_cyan,linear_black,feedback,turn_f,blue_dir,red_dir,yellow_dir,cyan_dir,black_dir,choice,start_choice,flag,error,turn_bis,turn_ter,error_2,err,err_1,err_2,err_3,second_obj):
    rand_number = [red_dir.value, yellow_dir.value, cyan_dir.value, black_dir.value]
    
    def random_choice (number, e, e_1, e_2, e_3):
        import numpy as np
        np.random.seed(1900)
        choice = np.random.choice(number)
        if (choice == e or choice == e_1 or choice == e_2 or choice == e_3):
            number.remove(choice)
            return random_choice(number,e,e_1, e_2, e_3)
        elif (choice != e and choice != e_1 and choice != e_2 and choice != e_3):
            return choice
    
    if(linear_red.spiked):
        red_dir.value = 3
    if(linear_blu.spiked):
        blue_dir.value = 1
    if(linear_yellow.spiked):
        yellow_dir.value = 2
    if(linear_cyan.spiked):
        cyan_dir.value = 5
    if(linear_black.spiked):
        black_dir.value = 4
    if(feedback.spiked):
        turn_f.value = 1
    if(error.spiked):
        if(choice.value == 2):
            err.value = 2
        if (choice.value == 3):
            err_1.value = 3
        if (choice.value == 4):
            err_2.value = 4
        if (choice.value == 5):
            err_3.value = 5
        turn_bis.value = 1
        turn_ter.value = 1
        second_obj.value = 0
        
    if(error_2.spiked):
        red_dir.value = 0
        blue_dir.value = 0
        yellow_dir.value = 0
        cyan_dir.value = 0
        black_dir.value = 0
        choice.value = 0
        start_choice.value = 0
        turn_bis.value = 1
        turn_ter.value = 0
        second_obj.value = 0
    if(start_choice.value == 1 and choice.value == 0):
        choice.value = random_choice(rand_number,err.value,err_1.value,err_2.value,err_3.value)
    
        