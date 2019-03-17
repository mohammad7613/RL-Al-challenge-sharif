from Model import *
import numpy as np

def feature_extractor(world, is_in_preprocess):
    # this function extracts useful features from the environment to feed the Neural Net
    if is_in_preprocess is False:
        # do the normal thing:

        # handling features related to distance:(72)
        distance_features = np.zeros(72)
        k = 0
        for i in range(8):
            for j in range(i+1,9):
                # calculating start cell in accordance to i
                if i<4:
                    start_cell = world.my_heroes[i].current_cell
                elif i<8 :
                    start_cell = world.opp_heroes[i-4].current_cell
                else:
                    start_cell = world.map.get_cell(15,15)
                # calculating end cell in accordance to j
                if j<4:
                    end_cell = world.my_heroes[j].current_cell
                elif j<8 :
                    end_cell = world.opp_heroes[j-4].current_cell
                else:
                    end_cell = world.map.get_cell(15,15)
                distance_features[k] = world.manhattan_distance(start_cell,end_cell) / 60
                k = k +1
                distance_features[k] = int(world.is_in_vision(start_cell,end_cell))
                k = k +1

        # creating the objective zone features:(8 + 8)
        in_obj_zone_feature = np.zeros(8)
        in_respawn_zone_feature = np.zeros(8)
        k = 0
        for itr in world.my_heroes:
            in_obj_zone_feature[k] = int(itr.current_cell.is_in_objective_zone)
            in_respawn_zone_feature[k] = int(itr.current_cell.is_in_my_respawn_zone)
            k = k + 1
        for itr in world.opp_heroes:
            in_obj_zone_feature[k] = int(itr.current_cell.is_in_objective_zone)
            in_respawn_zone_feature[k] = int(itr.current_cell.is_in_opp_respawn_zone)
            k = k + 1
        # counting the number of in vision cells: (1)
        # counting on the fact that cell in vision parameters is correct :
        in_vision_count =0
        wall_count =0
        for cell in world.map.cells:
            if cell.is_in_vision is True:
                in_vision_count = in_vision_count +1
            if cell.is_wall is True:
                wall_count = wall_count + 1
        in_vision_feature = in_vision_count / (31*31 - wall_count)
        # ap , turn and score features: (3)
        ap_feature = world.ap / world.max_ap
        turn_feature = world.current_turn / world.max_turns
        score_feature = (world.my_score - world.opp_score) / world.max_score
        #special abilities cool down feature(8):





        return
    else:
        # return features for every possible combinations of picks for both sides:
        actions = np.arange(0, 4)
        all_possible_actions = np.array(np.meshgrid(actions, actions, actions, actions, actions, actions, actions, actions)).T.reshape(-1, 8)

        return