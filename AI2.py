
from Model import *
from random import randint
import numpy as np
import time
from queue import Queue
def get_path_move_directions(start_cell, end_cell, world):
    # doing a bfs from start until reaching end cell while keeping parents:

    visited_flag = np.zeros(31 ** 2)
    parents = {}
    path = []
    my_hero_pos = []
    for hero in world.my_heroes:
        my_hero_pos.append(hero.current_cell)
    front = Queue()
    front.put(start_cell)
    visited_flag[start_cell.row * 31 + start_cell.column] = 1

    while front.empty() is False:
        top = front.get()
        if top == end_cell:
            # initializing parent finder :
            while top != start_cell:
                parent = parents[top]
                if top.row < parent.row:
                    path.append(Direction.UP)
                elif top.row > parent.row:
                    path.append(Direction.DOWN)
                elif top.column > parent.column:
                    path.append(Direction.RIGHT)
                elif top.column < parent.column:
                    path.append(Direction.LEFT)
                top = parent
            path.reverse()
            return path

        if top.row < 30:
            new_cell = world.map.get_cell(row=top.row + 1, column=top.column)
            if visited_flag[new_cell.row * 31 + new_cell.column] == 0 and new_cell.is_wall is False:
                is_hero_in_new_cell = False
                for itr in my_hero_pos:
                    if itr == new_cell:
                        is_hero_in_new_cell = True
                if is_hero_in_new_cell is False:
                    visited_flag[new_cell.row * 31 + new_cell.column] = 1
                    parents[new_cell] = top
                    front.put(new_cell)
        if top.row > 0:
            new_cell = world.map.get_cell(row=top.row - 1, column=top.column)
            if visited_flag[new_cell.row * 31 + new_cell.column] == 0 and new_cell.is_wall is False:
                is_hero_in_new_cell = False
                for itr in my_hero_pos:
                    if itr == new_cell:
                        is_hero_in_new_cell = True
                if is_hero_in_new_cell is False:
                    visited_flag[new_cell.row * 31 + new_cell.column] = 1
                    parents[new_cell] = top
                    front.put(new_cell)
        if top.column < 30:
            new_cell = world.map.get_cell(row=top.row, column=top.column + 1)
            if visited_flag[new_cell.row * 31 + new_cell.column] == 0 and new_cell.is_wall is False:
                is_hero_in_new_cell = False
                for itr in my_hero_pos:
                    if itr == new_cell:
                        is_hero_in_new_cell = True
                if is_hero_in_new_cell is False:
                    visited_flag[new_cell.row * 31 + new_cell.column] = 1
                    parents[new_cell] = top
                    front.put(new_cell)
        if top.column > 0:
            new_cell = world.map.get_cell(row=top.row, column=top.column - 1)
            if visited_flag[new_cell.row * 31 + new_cell.column] == 0 and new_cell.is_wall is False:
                is_hero_in_new_cell = False
                for itr in my_hero_pos:
                    if itr == new_cell:
                        is_hero_in_new_cell = True
                if is_hero_in_new_cell is False:
                    visited_flag[new_cell.row * 31 + new_cell.column] = 1
                    parents[new_cell] = top
                    front.put(new_cell)

    return path

class AI2:



    def preprocess(self, world):

        print("preprocess")

    def pick(self, world):
        print("pick")
        J=world.my_heroes
        print("im in pick AI3")
        world.pick_hero(HeroName.BLASTER)
        world.pick_hero(HeroName.BLASTER)
        world.pick_hero(HeroName.BLASTER)
        world.pick_hero(HeroName.BLASTER)

    def move(self, world):
        print("move")
        c = world.map.objective_zone
        res=world.map.my_respawn_zone
        ####################################
        OPCEL=[0,0,0,0]
        OPROW=[0,0,0,0]
        OPCOL=[0,0,0,0]
        i=0
        for ophero in world.opp_heroes:
            opcel = ophero.current_cell
            row = opcel.row
            if row != -1:
              OPCEL[i] = ophero.current_cell
              OPCOL[i]=OPCEL[i].column
              OPROW[i]= OPCEL[i].row
            i = i + 1
       ################################
        CEL=[0,0,0,0]
        COL=[0,0,0,0]
        ROW=[0,0,0,0]
        i=0
        for hero in world.my_heroes:
            CEL[i] = hero.current_cell
            COL[i] =  CEL[i].column
            ROW[i] =  CEL[i].row
            i = i + 1
        ##################################################################

        ol = 0
        for cell in c:
            if OPCOL[0] != 0 and OPROW[0] != -1:
                if cell == OPCEL[0]:
                    ol = ol + 1
                    break
        ol1 = 0
        for cell in c:
            if OPCOL[1] != 0 and OPROW[1] != -1:
                if cell == OPCEL[1]:
                    ol1 = ol1 + 1
                    break
        ol2 = 0
        for cell in c:
            if OPCOL[2] != 0 and OPROW[2] != -1:
                if cell == OPCEL[2]:
                    ol2 = ol2 + 1
                    break
        ol3 = 0
        for cell in c:
            if OPCOL[3] != 0 and OPROW[3] != -1:
                if cell == OPCEL[3]:
                    ol3 = ol3 + 1
                    break
        FAZ =world.move_phase_num
        #############################################################
        U = len(c)
        A=U//2
        V=U//4
        VV=(U//4)*3
        E=[]
        T=[]
        for cel in c:
            ui=cel.row
            iu=cel.column
            E.append(ui)
            T.append(iu)
        mxro=max(E)
        mxco=max(T)
        miro=min(E)
        mico=min(T)
        R=c[0].row
        C=c[0].column
        G = []
        H = []
        M = []
        N = []
        for cel in c:
            r=cel.row
            cl=cel.column
            if r>=miro and r<=((mxro+miro)//2) and cl>=mico and cl<=((mxco+mico)//2):
                G.append(cel)
            elif r>(((mxro+miro)//2)) and cl>=mico and cl<=((mxco+mico)//2):
                H.append(cel)
            elif r>(((mxro+miro)//2)) and cl>((mxco+mico)//2) :
                N.append(cel)
            elif r>=miro and r<=((mxro+miro)//2) and cl>((mxco+mico)//2) :
                M.append(cel)
        if world.my_heroes[0].current_hp > 0:
           DO = get_path_move_directions(start_cell=CEL[0],end_cell=G[3],world=world)
        if world.my_heroes[1].current_hp>0:
           DO1 =get_path_move_directions(start_cell=CEL[1], end_cell=H[3] ,world=world)
        if world.my_heroes[2].current_hp > 0:
           DO2 = get_path_move_directions(start_cell=CEL[2], end_cell=M[1] ,world=world)
        if world.my_heroes[3].current_hp > 0:
           DO3 = get_path_move_directions(start_cell=CEL[3], end_cell=N[2] ,world=world)
        l = 0
        for cell in G:
            if cell == CEL[0]:
                l = l + 1
                break
        l1 = 0
        for cell in H:
            if cell == CEL[1]:
                l1 = l + 1
                break
        l2 = 0
        for cell in M:
            if cell == CEL[2]:
                l2 = l + 1
                break
        l3 = 0
        for cell in N:
            if cell == CEL[3]:
                l3 = l + 1
                break
        # i=0
        # for cel in c:
        #     i=i+1
        #     if i<(V+1):
        #         G.append(cel)
        #     elif i>(V) and i<(A+1):
        #         H.append(cel)
        #     elif i > (A) and i<(VV+1)   :
        #         M.append(cel)
        #     elif i>(VV):
        #         N.append(cel)


        #####################################################################
        f = AbilityName.BLASTER_BOMB
        h = world.my_heroes[0].get_ability(f).is_ready()
        h1 = world.my_heroes[1].get_ability(f).is_ready()
        h2 = world.my_heroes[2].get_ability(f).is_ready()
        h3 = world.my_heroes[3].get_ability(f).is_ready()
        #####################################################################
        fa = AbilityName.BLASTER_ATTACK
        hh = world.my_heroes[0].get_ability(fa).is_ready()
        hh1 = world.my_heroes[1].get_ability(fa).is_ready()
        hh2 = world.my_heroes[2].get_ability(fa).is_ready()
        hh3 = world.my_heroes[3].get_ability(fa).is_ready()
        ######################################################################
        faa = AbilityName.BLASTER_DODGE
        hhh = world.my_heroes[0].get_ability(faa).is_ready()
        hhh1 = world.my_heroes[1].get_ability(faa).is_ready()
        hhh2 = world.my_heroes[2].get_ability(faa).is_ready()
        hhh3 = world.my_heroes[3].get_ability(faa).is_ready()
        ########################################################################
        # if CEL[0].is_in_my_respawn_zone :
        #     j=CEL[0].row
        #     b = CEL[0].column
        #     PR=[j,j+1,j+2,j+3,j+4,j-1,j-2,j-3,j-4]
        #     PC=[b,b+1,b+2,b+3,b+4,b-1,b-2,b-3,b-4]
        #     for r in PR:
        #         for c in PC:
        #            if world.manhattan_distance(start_cell_row=j,start_cell_column=b,end_cell_row=r,end_cell_column=c) <5:
        #
        ded=world.get_my_dead_heroes()
        if len(ded)>0:
            bb = 0
            uuuu=0
            uuu = 0
            D = 0
            if h1 is True and uuu == 0 and l1 != 0 and D == 0 and world.my_heroes[1].current_hp > 0:
                good4 = []
                good1 = []
                good2 = []
                good3 = []
                uuu = 0
                bb = 0
                for cel in H:
                    j = 0
                    if OPCOL[0] != 0:
                        if world.manhattan_distance(start_cell=cel, end_cell=OPCEL[0]) < 3:
                            j = j + 1
                    if OPCOL[1] != 0:
                        if world.manhattan_distance(start_cell=cel, end_cell=OPCEL[1]) < 3:
                            j = j + 1
                    if OPCOL[2] != 0:
                        if world.manhattan_distance(start_cell=cel, end_cell=OPCEL[2]) < 3:
                            j = j + 1
                    if OPCOL[3] != 0:
                        if world.manhattan_distance(start_cell=cel, end_cell=OPCEL[3]) < 3:
                            j = j + 1
                    if j == 4:
                        good4.append(cel)

                    elif j == 3:
                        good3.append(cel)

                    elif j == 2:
                        good2.append(cel)

                    elif j == 1:
                        good1.append(cel)
                if len(good4) > 0:
                    ff = []
                    B = []
                    for gd in good4:
                        ff = []
                        B = []
                        if world.manhattan_distance(start_cell=CEL[1], end_cell=gd) < 6:
                            bb = 1
                            break
                        elif uuu == 0 and bb == 0:
                            ff = []
                            B = []
                            for cel in H:
                                if world.manhattan_distance(cel, gd) < 6:
                                    ff.append(cel)
                    if bb == 0:
                        for fff in ff:
                            dg =get_path_move_directions(start_cell=CEL[1], end_cell=fff ,world=world)
                            B.append(len(dg))
                        if len(B) > 0:
                            Y = B.index(min(B))
                            if (B[Y] + FAZ - 1) < 7 and bb == 0:
                                dg = get_path_move_directions(start_cell=CEL[1], end_cell=ff[Y],world=world)
                                if len(dg) > 0:
                                    world.move_hero(hero=world.my_heroes[1], direction=dg[0])
                                    uuu = 1
                elif uuu == 0 and bb == 0 and len(good3) > 0:
                    ff = []
                    B = []
                    for gd in good3:
                        ff = []
                        B = []
                        if world.manhattan_distance(CEL[1], gd) < 6:
                            bb = 1
                            break
                        elif uuu == 0 and bb == 0:
                            ff = []
                            B = []
                            for cel in H:
                                if world.manhattan_distance(cel, gd) < 6:
                                    ff.append(cel)
                    if bb == 0:
                        for fff in ff:
                            dg = get_path_move_directions(start_cell=CEL[1], end_cell=fff ,world=world)
                            B.append(len(dg))
                        if len(B) > 0:
                            Y = B.index(min(B))
                            if (B[Y] + FAZ - 1) < 7:
                                dg = get_path_move_directions(start_cell=CEL[1], end_cell=ff[Y] , world=world)
                                if len(dg) > 0:
                                    world.move_hero(hero=world.my_heroes[1], direction=dg[0])
                                    uuu = 1
                elif uuu == 0 and bb == 0 and len(good2) > 0:
                    fff2 = []
                    BB2 = []
                    for gd in good2:
                        fff2 = []
                        BB2 = []
                        if world.manhattan_distance(CEL[1], gd) < 6:
                            bb = 1
                            break
                        elif uuu == 0 and bb == 0:
                            fff2 = []
                            BB2 = []
                            for cel in H:
                                if world.manhattan_distance(cel, gd) < 6:
                                    fff2.append(cel)
                    if bb == 0:
                        for fff in fff2:
                            dg = get_path_move_directions(start_cell=CEL[1], end_cell=fff , world=world)
                            BB2.append(len(dg))
                        if len(BB2) > 0:
                            Y = BB2.index(min(BB2))
                            if (BB2[Y] + FAZ - 1) < 7:
                                dg = get_path_move_directions(start_cell=CEL[1], end_cell=fff2[Y] , world=world)
                                if len(dg) > 0:
                                    world.move_hero(hero=world.my_heroes[1], direction=dg[0])
                                    uuu = 1
                elif uuu == 0 and bb == 0 and len(good1) > 0:
                    fff1 = []
                    BB1 = []
                    for gd in good1:
                        fff1 = []
                        BB1 = []
                        if world.manhattan_distance(CEL[1], gd) < 6:
                            bb = 1
                            break
                        elif uuu == 0 and bb == 0:
                            fff1 = []
                            BB1 = []
                            for cel in H:
                                if world.manhattan_distance(cel, gd) < 6:
                                    fff1.append(cel)
                    if bb == 0:
                        for fff in fff1:
                            dg = get_path_move_directions(start_cell=CEL[1], end_cell=fff , world=world)
                            BB1.append(len(dg))
                        if len(BB1) > 0:
                            Y = BB1.index(min(BB1))
                            if (BB1[Y] + FAZ - 1) < 7:
                                dg = get_path_move_directions(start_cell=CEL[1], end_cell=fff1[Y] , world=world)
                                if len(dg) > 0:
                                    world.move_hero(hero=world.my_heroes[1], direction=dg[0])
                                    uuu = 1
            # if hhh1 is True and  bb == 0 and uuuu==0:
            #     uuuu = 0
            #     if OPCOL[0] != 0 and uuuu == 0:
            #         if world.opp_heroes[0].name == HeroName.BLASTER:
            #             ti = world.opp_heroes[0].get_ability(f).is_ready()
            #             if ti is True:
            #                 if world.manhattan_distance(CEL[1], OPCEL[0]) < 8:
            #                     for cel in H:
            #                         if world.manhattan_distance(start_cell=CEL[1], end_cell=cel) > 2 and cel != CEL[0] and cel != CEL[2] and cel != CEL[3] and uuuu == 0:
            #                             uuuu = 1
            #                             break
            #     if OPCOL[1] != 0 and uuuu == 0:
            #         if world.opp_heroes[1].name == HeroName.BLASTER:
            #             ti = world.opp_heroes[1].get_ability(f).is_ready()
            #             if ti is True:
            #                 if world.manhattan_distance(CEL[1], OPCEL[1]) < 8:
            #                     for cel in H:
            #                         if world.manhattan_distance(start_cell=CEL[1], end_cell=cel) > 2 and cel != CEL[0] and cel != CEL[2] and cel != CEL[3] and uuuu == 0:
            #                             uuuu = 1
            #                             break
            #     if OPCOL[2] != 0 and uuuu == 0:
            #         if world.opp_heroes[2].name == HeroName.BLASTER:
            #             ti = world.opp_heroes[2].get_ability(f).is_ready()
            #             if ti is True:
            #                 if world.manhattan_distance(CEL[1], OPCEL[2]) < 8:
            #                     for cel in H:
            #                         if world.manhattan_distance(start_cell=CEL[1], end_cell=cel) > 2 and cel != CEL[0] and cel != CEL[2] and cel != CEL[3] and uuuu == 0:
            #                             uuuu = 1
            #                             break
            #     if OPCOL[3] != 0 and uuuu == 0:
            #         if world.opp_heroes[3].name == HeroName.BLASTER:
            #             ti = world.opp_heroes[3].get_ability(f).is_ready()
            #             if ti is True:
            #                 if world.manhattan_distance(CEL[1], OPCEL[3]) < 8:
            #                     for cel in H:
            #                         if world.manhattan_distance(start_cell=CEL[1], end_cell=cel) > 2 and cel != CEL[0] and cel != CEL[2] and cel != CEL[3] and uuuu == 0:
            #                             uuuu = 1
            #                             break
            if hh1 is True and uuu == 0 and bb == 0 and l1 != 0 and D == 0 and hhh1 is False and uuuu==0 and h1 is False and world.my_heroes[1].current_hp > 0:
                Q = []
                for cel in H:
                    K = 0
                    if OPCOL[0] != 0:
                        if world.get_impact_cell(ability=world.my_heroes[1].get_ability(fa), start_cell=cel,target_cell=OPCEL[0]) == OPCEL[0]:
                            Q.append(cel)
                            K = 1
                    if OPCOL[1] != 0 and K == 0:
                        if world.get_impact_cell(ability=world.my_heroes[1].get_ability(fa), start_cell=cel,target_cell=OPCEL[1]) == OPCEL[1]:
                            Q.append(cel)
                            K = 1
                    if OPCOL[2] != 0 and K == 0:
                        if world.get_impact_cell(ability=world.my_heroes[1].get_ability(fa), start_cell=cel,target_cell=OPCEL[2]) == OPCEL[2]:
                            Q.append(cel)
                            K = 1
                    if OPCOL[3] != 0 and K == 0:
                        if world.get_impact_cell(ability=world.my_heroes[1].get_ability(fa), start_cell=cel,target_cell=OPCEL[3]) == OPCEL[3]:
                            Q.append(cel)
                            K = 1
                i = 0
                bbbb = []
                ww = 1000
                bbbb.clear()
                D = 0
                if len(Q) > 0:
                    for q in Q:
                        if q == CEL[1]:
                            D = 1
                            break
                        else:
                            e = get_path_move_directions(start_cell=CEL[1], end_cell=q , world=world)
                            s = len(e)
                            bbbb.append(s)
                    if len(bbbb) > 0:
                        a = bbbb.index(min(bbbb))
                        if D == 0:
                            e = get_path_move_directions(start_cell=CEL[1], end_cell=Q[a] , world=world)
                            if len(e) > 0 and (len(e) + FAZ - 1) < 7:
                                world.move_hero(hero=world.my_heroes[1], direction=e[0])
                                uuu = 1
            # if hhh1 is False and uuu == 0 and bb == 0 and l1 != 0 and D == 0:
            #     i = 0
            #     j = 0
            #     good4 = []
            #     good1 = []
            #     good2 = []
            #     good3 = []
            #     good = []
            #     uuu = 0
            #     bb = 0
            #     for cel in H:
            #         j = 0
            #         if OPCOL[0] != 0:
            #             if world.manhattan_distance(cel, OPCEL[0]) > 5:
            #                 j = j + 1
            #         elif OPCOL[0] == 0:
            #             j = j + 1
            #         if OPCOL[1] != 0:
            #             if world.manhattan_distance(cel, OPCEL[1]) > 5:
            #                 j = j + 1
            #         elif OPCOL[1] == 0:
            #             j = j + 1
            #         if OPCOL[2] != 0:
            #             if world.manhattan_distance(cel, OPCEL[2]) > 5:
            #                 j = j + 1
            #         elif OPCOL[2] == 0:
            #             j = j + 1
            #         if OPCOL[3] != 0:
            #             if world.manhattan_distance(cel, OPCEL[3]) > 5:
            #                 j = j + 1
            #         elif OPCOL[3] == 0:
            #             j = j + 1
            #         if j == 4:
            #             good4.append(cel)
            #
            #         elif j == 3:
            #             good3.append(cel)
            #
            #         elif j == 2:
            #             good2.append(cel)
            #
            #         elif j == 1:
            #             good1.append(cel)
            #     if len(good4) != 0:
            #         ff = []
            #         B = []
            #         for gd in good4:
            #             if gd == CEL[1]:
            #                 bb = 1
            #                 break
            #             else:
            #                 ss = world.get_path_move_directions(start_cell=CEL[1], end_cell=gd)
            #                 if (len(ss) + FAZ - 1) < 7:
            #                     ff.append(gd)
            #         if bb == 0 and len(ff) > 0:
            #             for fff in ff:
            #                 dg = world.get_path_move_directions(start_cell=CEL[1], end_cell=fff)
            #                 B.append(len(dg))
            #             if len(B) > 0:
            #                 Y = B.index(min(B))
            #                 if (B[Y] + FAZ - 1) < 7:
            #                     dg = world.get_path_move_directions(start_cell=CEL[1], end_cell=ff[Y])
            #                     if len(dg) > 0:
            #                         world.move_hero(hero=world.my_heroes[1], direction=dg[0])
            #                         uuu = 1
            #
            #
            #     elif uuu == 0 and bb == 0 and len(good3) > 0:
            #         ff = []
            #         B = []
            #         for gd in good3:
            #             if gd == CEL[1]:
            #                 bb = 1
            #                 break
            #             else:
            #                 ss = world.get_path_move_directions(start_cell=CEL[1], end_cell=gd)
            #                 if (len(ss) + FAZ - 1) < 7:
            #                     ff.append(gd)
            #         if bb == 0 and len(ff) > 0:
            #             for fff in ff:
            #                 dg = world.get_path_move_directions(start_cell=CEL[1], end_cell=fff)
            #                 B.append(len(dg))
            #             if len(B) > 0:
            #                 Y = B.index(min(B))
            #                 if (B[Y] + FAZ - 1) < 7:
            #                     dg = world.get_path_move_directions(start_cell=CEL[1], end_cell=ff[Y])
            #                     if len(dg) > 0:
            #                         world.move_hero(hero=world.my_heroes[1], direction=dg[0])
            #                         uuu = 1
            #
            #
            #     elif uuu == 0 and bb == 0 and len(good2) > 0:
            #         ff = []
            #         B = []
            #         for gd in good2:
            #             if gd == CEL[1]:
            #                 bb = 1
            #                 break
            #             else:
            #                 ss = world.get_path_move_directions(start_cell=CEL[1], end_cell=gd)
            #                 if (len(ss) + FAZ - 1) < 7:
            #                     ff.append(gd)
            #         if bb == 0 and len(ff) > 0:
            #             for fff in ff:
            #                 dg = world.get_path_move_directions(start_cell=CEL[1], end_cell=fff)
            #                 B.append(len(dg))
            #             if len(B) > 0:
            #                 Y = B.index(min(B))
            #                 if (B[Y] + FAZ - 1) < 7:
            #                     dg = world.get_path_move_directions(start_cell=CEL[1], end_cell=ff[Y])
            #                     if len(dg) > 0:
            #                         world.move_hero(hero=world.my_heroes[1], direction=dg[0])
            #                         uuu = 1
            #
            #
            #     elif uuu == 0 and bb == 0 and len(good1) > 0:
            #         ff = []
            #         B = []
            #         for gd in good1:
            #             if gd == CEL[1]:
            #                 bb = 1
            #                 break
            #             else:
            #                 ss = world.get_path_move_directions(start_cell=CEL[1], end_cell=gd)
            #                 if (len(ss) + FAZ - 1) < 7:
            #                     ff.append(gd)
            #         if bb == 0 and len(ff) > 0:
            #             for fff in ff:
            #                 dg = world.get_path_move_directions(start_cell=CEL[1], end_cell=fff)
            #                 B.append(len(dg))
            #             if len(B) > 0:
            #                 Y = B.index(min(B))
            #                 if (B[Y] + FAZ - 1) < 7:
            #                     dg = world.get_path_move_directions(start_cell=CEL[1], end_cell=ff[Y])
            #                     if len(dg) > 0:
            #                         world.move_hero(hero=world.my_heroes[1], direction=dg[0])
            #                         uuu = 1
            if uuu == 0 and bb == 0 and D == 0 and uuuu==0 and world.my_heroes[1].current_hp > 0 and l1==0:
                if len(DO1) > 0:
                    world.move_hero(hero=world.my_heroes[1], direction=DO1[0])
                    uuu = 1
            uuu = 0
            bb = 0
            D = 0
            uuuu = 0
            if h is True and uuu == 0 and l != 0 and D == 0 and world.my_heroes[0].current_hp > 0:
                i = 0
                j = 0
                good4 = []
                good1 = []
                good2 = []
                good3 = []
                uuu = 0
                bb = 0
                for cel in G:
                    j = 0
                    if OPCOL[0] != 0:
                        if world.manhattan_distance(cel, OPCEL[0]) < 3:
                            j = j + 1
                    if OPCOL[1] != 0:
                        if world.manhattan_distance(cel, OPCEL[1]) < 3:
                            j = j + 1
                    if OPCOL[2] != 0:
                        if world.manhattan_distance(cel, OPCEL[2]) < 3:
                            j = j + 1
                    if OPCOL[3] != 0:
                        if world.manhattan_distance(cel, OPCEL[3]) < 3:
                            j = j + 1
                    if j == 4:
                        good4.append(cel)

                    elif j == 3:
                        good3.append(cel)

                    elif j == 2:
                        good2.append(cel)

                    elif j == 1:
                        good1.append(cel)
                if len(good4) != 0:
                    ff = []
                    B = []
                    for gd in good4:
                        if world.manhattan_distance(CEL[0], gd) < 6:
                            bb = 1
                            break
                        else:
                            for cel in G:
                                if world.manhattan_distance(cel, gd) < 6:
                                    ff.append(cel)
                    if bb == 0 and uuu == 0:
                        for fff in ff:
                            dg = get_path_move_directions(start_cell=CEL[0], end_cell=fff , world=world)
                            B.append(len(dg))
                        if len(B) > 0:
                            Y = B.index(min(B))
                            if (B[Y] + FAZ - 1) < 7:
                                dg = get_path_move_directions(start_cell=CEL[0], end_cell=ff[Y] ,  world=world)
                                if len(dg) > 0:
                                    world.move_hero(hero=world.my_heroes[0], direction=dg[0])
                                    uuu = 1

                elif uuu == 0 and bb == 0 and len(good3) > 0:
                    ff = []
                    B = []
                    for gd in good3:
                        if world.manhattan_distance(CEL[0], gd) < 6:
                            bb = 1
                            break
                        else:
                            for cel in G:
                                if world.manhattan_distance(cel, gd) < 6:
                                    ff.append(cel)
                    if bb == 0 and uuu == 0:
                        for fff in ff:
                            dg =get_path_move_directions(start_cell=CEL[0], end_cell=fff , world=world)
                            B.append(len(dg))
                        if len(B) > 0:
                            Y = B.index(min(B))
                            if (B[Y] + FAZ - 1) < 7:
                                dg =get_path_move_directions(start_cell=CEL[0], end_cell=ff[Y] ,  world=world)
                                if len(dg) > 0:
                                    world.move_hero(hero=world.my_heroes[0], direction=dg[0])
                                    uuu = 1
                elif uuu == 0 and bb == 0 and len(good2) > 0:
                    fff2 = []
                    BB2 = []
                    for gd in good2:
                        if world.manhattan_distance(CEL[0], gd) < 6:
                            bb = 1
                            break
                        else:
                            for cel in G:
                                if world.manhattan_distance(cel, gd) < 6:
                                    fff2.append(cel)
                    if bb == 0 and uuu == 0:
                        for fff in fff2:
                            dg =get_path_move_directions(start_cell=CEL[0], end_cell=fff , world=world)
                            BB2.append(len(dg))
                        if len(BB2) > 0:
                            Y = BB2.index(min(BB2))
                            if (BB2[Y] + FAZ - 1) < 7:
                                dg = get_path_move_directions(start_cell=CEL[0], end_cell=fff2[Y] , world=world)
                                if len(dg) > 0:
                                    world.move_hero(hero=world.my_heroes[0], direction=dg[0])
                                    uuu = 1


                elif uuu == 0 and bb == 0 and len(good1) > 0:
                    fff1 = []
                    BB1 = []
                    for gd in good1:
                        if world.manhattan_distance(CEL[0], gd) < 6:
                            bb = 1
                            break
                        else:
                            for cel in G:
                                if world.manhattan_distance(cel, gd) < 6:
                                    fff1.append(cel)
                    if bb == 0 and uuu == 0:
                        for fff in fff1:
                            dg = get_path_move_directions(start_cell=CEL[0], end_cell=fff , world=world)
                            BB1.append(len(dg))
                        if len(BB1) > 0:
                            Y = BB1.index(min(BB1))
                            if (BB1[Y] + FAZ - 1) < 7:
                                dg = get_path_move_directions(start_cell=CEL[0], end_cell=fff1[Y] , world=world)
                                if len(dg) > 0:
                                    world.move_hero(hero=world.my_heroes[0], direction=dg[0])
                                    uuu = 1
            # if hhh is True and  bb ==0 and uuuu==0 :
            #     uuuu = 0
            #     if OPCOL[0] != 0 and uuuu == 0:
            #         if world.opp_heroes[0].name == HeroName.BLASTER:
            #             ti = world.opp_heroes[0].get_ability(f).is_ready()
            #             if ti is True:
            #                 if world.manhattan_distance(CEL[0], OPCEL[0]) < 8:
            #                     for cel in G:
            #                         if world.manhattan_distance(start_cell=CEL[0], end_cell=cel) > 2 and cel != CEL[1] and cel != CEL[2] and cel != CEL[3] and uuuu == 0:
            #                             uuuu = 1
            #                             break
            #     if OPCOL[1] != 0 and uuuu == 0:
            #         if world.opp_heroes[1].name == HeroName.BLASTER:
            #             ti = world.opp_heroes[1].get_ability(f).is_ready()
            #             if ti is True:
            #                 if world.manhattan_distance(CEL[0], OPCEL[1]) < 8:
            #                     for cel in G:
            #                         if world.manhattan_distance(start_cell=CEL[0], end_cell=cel) > 2 and cel != CEL[1] and cel != CEL[2] and cel != CEL[3] and uuuu == 0:
            #                             uuuu = 1
            #                             break
            #     if OPCOL[2] != 0 and uuuu == 0:
            #         if world.opp_heroes[2].name == HeroName.BLASTER:
            #             ti = world.opp_heroes[2].get_ability(f).is_ready()
            #             if ti is True:
            #                 if world.manhattan_distance(CEL[0], OPCEL[2]) < 8:
            #                     for cel in G:
            #                         if world.manhattan_distance(start_cell=CEL[0], end_cell=cel) > 2 and cel != CEL[1] and cel != CEL[2] and cel != CEL[3] and uuuu == 0:
            #                             uuuu = 1
            #                             break
            #     if OPCOL[3] != 0 and uuuu == 0:
            #         if world.opp_heroes[3].name == HeroName.BLASTER:
            #             ti = world.opp_heroes[3].get_ability(f).is_ready()
            #             if ti is True:
            #                 if world.manhattan_distance(CEL[0], OPCEL[3]) < 8:
            #                     for cel in G:
            #                         if world.manhattan_distance(start_cell=CEL[0], end_cell=cel) > 2 and cel != CEL[1] and cel != CEL[2] and cel != CEL[3] and uuuu == 0:
            #                             uuuu = 1
            #                             break
            if hh is True and uuu == 0 and bb == 0 and l != 0 and D == 0 and uuuu==0 and hhh is False and h is False and world.my_heroes[0].current_hp > 0:
                Q = []
                for cel in G:
                    K = 0
                    if OPCOL[0] != 0:
                        if world.get_impact_cell(ability=world.my_heroes[0].get_ability(fa), start_cell=cel,target_cell=OPCEL[0]) == OPCEL[0]:
                            Q.append(cel)
                            K = 1
                    if OPCOL[1] != 0 and K == 0:
                        if world.get_impact_cell(ability=world.my_heroes[0].get_ability(fa), start_cell=cel,target_cell=OPCEL[1]) == OPCEL[1]:
                            Q.append(cel)
                            K = 1
                    if OPCOL[2] != 0 and K == 0:
                        if world.get_impact_cell(ability=world.my_heroes[0].get_ability(fa), start_cell=cel,target_cell=OPCEL[2]) == OPCEL[2]:
                            Q.append(cel)
                            K = 1
                    if OPCOL[3] != 0 and K == 0:
                        if world.get_impact_cell(ability=world.my_heroes[0].get_ability(fa), start_cell=cel,target_cell=OPCEL[3]) == OPCEL[3]:
                            Q.append(cel)
                            K = 1
                i = 0
                bbbb = []
                bbbb.clear()
                D = 0
                if len(Q) > 0:
                    for q in Q:
                        if q == CEL[0]:
                            D = 1
                            break
                        else:
                            e = get_path_move_directions(start_cell=CEL[0], end_cell=q , world=world)
                            s = len(e)
                            bbbb.append(s)
                    if len(bbbb) > 0:
                        a = bbbb.index(min(bbbb))
                        if D == 0:
                            e = get_path_move_directions(start_cell=CEL[0], end_cell=Q[a] , world=world)
                            if len(e) > 0 and (len(e) + FAZ - 1) < 7:
                                world.move_hero(hero=world.my_heroes[0], direction=e[0])
                                uuu = 1
            # if hhh is False and uuu == 0 and bb == 0 and l != 0 and D == 0:
            #     i = 0
            #     j = 0
            #     good4 = []
            #     good1 = []
            #     good2 = []
            #     good3 = []
            #     uuu = 0
            #     bb = 0
            #     for cel in G:
            #         j = 0
            #         if OPCOL[0] != 0:
            #             if world.manhattan_distance(cel, OPCEL[0]) > 5:
            #                 j = j + 1
            #         elif OPCOL[0] == 0:
            #             j = j + 1
            #
            #         if OPCOL[1] != 0:
            #             if world.manhattan_distance(cel, OPCEL[1]) > 5:
            #                 j = j + 1
            #         elif OPCOL[1] == 0:
            #             j = j + 1
            #         if OPCOL[2] != 0:
            #             if world.manhattan_distance(cel, OPCEL[2]) > 5:
            #                 j = j + 1
            #         elif OPCOL[2] == 0:
            #             j = j + 1
            #         if OPCOL[3] != 0:
            #             if world.manhattan_distance(cel, OPCEL[3]) > 5:
            #                 j = j + 1
            #         elif OPCOL[3] == 0:
            #             j = j + 1
            #         if j == 4:
            #             good4.append(cel)
            #
            #         elif j == 3:
            #             good3.append(cel)
            #
            #         elif j == 2:
            #             good2.append(cel)
            #
            #         elif j == 1:
            #             good1.append(cel)
            #     if len(good4) != 0:
            #         ff = []
            #         B = []
            #         for gd in good4:
            #             if gd == CEL[0]:
            #                 bb = 1
            #                 break
            #             else:
            #                 ss = world.get_path_move_directions(start_cell=CEL[0], end_cell=gd)
            #                 if (len(ss) + FAZ - 1) < 7:
            #                     ff.append(gd)
            #         for fff in ff:
            #             dg = world.get_path_move_directions(start_cell=CEL[0], end_cell=fff)
            #             B.append(len(dg))
            #         if len(B) > 0:
            #             Y = B.index(min(B))
            #             if (B[Y] + FAZ - 1) < 7:
            #                 dg = world.get_path_move_directions(start_cell=CEL[0], end_cell=ff[Y])
            #                 if len(dg) > 0:
            #                     world.move_hero(hero=world.my_heroes[0], direction=dg[0])
            #                     uuu = 1
            #
            #     elif uuu == 0 and bb == 0 and len(good3) > 0:
            #         ff = []
            #         B = []
            #         for gd in good3:
            #             if gd == CEL[0]:
            #                 bb = 1
            #                 break
            #             else:
            #                 ss = world.get_path_move_directions(start_cell=CEL[0], end_cell=gd)
            #                 if (len(ss) + FAZ - 1) < 7:
            #                     ff.append(gd)
            #         for fff in ff:
            #             dg = world.get_path_move_directions(start_cell=CEL[0], end_cell=fff)
            #             B.append(len(dg))
            #         if len(B) > 0:
            #             Y = B.index(min(B))
            #             if (B[Y] + FAZ - 1) < 7:
            #                 dg = world.get_path_move_directions(start_cell=CEL[0], end_cell=ff[Y])
            #                 if len(dg) > 0:
            #                     world.move_hero(hero=world.my_heroes[0], direction=dg[0])
            #                     uuu = 1
            #
            #     elif uuu == 0 and bb == 0 and len(good2) > 0:
            #         ff = []
            #         B = []
            #         for gd in good2:
            #             if gd == CEL[0]:
            #                 bb = 1
            #                 break
            #             else:
            #                 ss = world.get_path_move_directions(start_cell=CEL[0], end_cell=gd)
            #                 if (len(ss) + FAZ - 1) < 7:
            #                     ff.append(gd)
            #         for fff in ff:
            #             dg = world.get_path_move_directions(start_cell=CEL[0], end_cell=fff)
            #             B.append(len(dg))
            #         if len(B) > 0:
            #             Y = B.index(min(B))
            #             if (B[Y] + FAZ - 1) < 7:
            #                 dg = world.get_path_move_directions(start_cell=CEL[0], end_cell=ff[Y])
            #                 if len(dg) > 0:
            #                     world.move_hero(hero=world.my_heroes[0], direction=dg[0])
            #                     uuu = 1
            #
            #     elif uuu == 0 and bb == 0 and len(good1) > 0:
            #         ff = []
            #         B = []
            #         for gd in good1:
            #             if gd == CEL[0]:
            #                 bb = 1
            #                 break
            #             else:
            #                 ss = world.get_path_move_directions(start_cell=CEL[0], end_cell=gd)
            #                 if (len(ss) + FAZ - 1) < 7:
            #                     ff.append(gd)
            #         for fff in ff:
            #             dg = world.get_path_move_directions(start_cell=CEL[0], end_cell=fff)
            #             B.append(len(dg))
            #         if len(B) > 0:
            #             Y = B.index(min(B))
            #             if (B[Y] + FAZ - 1) < 7:
            #                 dg = world.get_path_move_directions(start_cell=CEL[0], end_cell=ff[Y])
            #                 if len(dg) > 0:
            #                     world.move_hero(hero=world.my_heroes[0], direction=dg[0])
            #                     uuu = 1
            if uuu == 0 and bb == 0 and D == 0 and uuuu==0 and world.my_heroes[0].current_hp > 0 and l==0:
                if len(DO) > 0:
                    world.move_hero(hero=world.my_heroes[0], direction=DO[0])
                    uuu = 1
            D = 0
            bb = 0
            uuu = 0
            uuuu = 0
            if h2 is True and uuu == 0 and l2 != 0 and D == 0 and world.my_heroes[2].current_hp > 0:
                i = 0
                j = 0
                good4 = []
                good1 = []
                good2 = []
                good3 = []
                uuu = 0
                bb = 0
                for cel in M:
                    j = 0
                    if OPCOL[0] != 0:
                        if world.manhattan_distance(cel, OPCEL[0]) < 3:
                            j = j + 1
                    if OPCOL[1] != 0:
                        if world.manhattan_distance(cel, OPCEL[1]) < 3:
                            j = j + 1
                    if OPCOL[2] != 0:
                        if world.manhattan_distance(cel, OPCEL[2]) < 3:
                            j = j + 1
                    if OPCOL[3] != 0:
                        if world.manhattan_distance(cel, OPCEL[3]) < 3:
                            j = j + 1
                    if j == 4:
                        good4.append(cel)

                    elif j == 3:
                        good3.append(cel)

                    elif j == 2:
                        good2.append(cel)

                    elif j == 1:
                        good1.append(cel)
                if len(good4) != 0:
                    ff = []
                    B = []
                    for gd in good4:
                        if world.manhattan_distance(CEL[2], gd) < 6:
                            bb = 1
                            break
                        else:
                            for cel in M:
                                if world.manhattan_distance(cel, gd) < 6:
                                    ff.append(cel)
                    if bb == 0 and uuu == 0:
                        for fff in ff:
                            dg = get_path_move_directions(start_cell=CEL[2], end_cell=fff , world=world)
                            B.append(len(dg))
                        if len(B) > 0:
                            Y = B.index(min(B))
                            if (B[Y] + FAZ - 1) < 7:
                                dg = get_path_move_directions(start_cell=CEL[2], end_cell=ff[Y] , world=world)
                                if len(dg) > 0:
                                    world.move_hero(hero=world.my_heroes[2], direction=dg[0])
                                    uuu = 1

                elif uuu == 0 and bb == 0 and len(good3) > 0:
                    ff = []
                    B = []
                    for gd in good3:
                        if world.manhattan_distance(CEL[2], gd) < 6:
                            bb = 1
                            break
                        else:
                            for cel in M:
                                if world.manhattan_distance(cel, gd) < 6:
                                    ff.append(cel)
                    if bb == 0 and uuu == 0:
                        for fff in ff:
                            dg = get_path_move_directions(start_cell=CEL[2], end_cell=fff , world=world)
                            B.append(len(dg))
                        if len(B) > 0:
                            Y = B.index(min(B))
                            if (B[Y] + FAZ - 1) < 7:
                                dg = get_path_move_directions(start_cell=CEL[2], end_cell=ff[Y] , world=world)
                                if len(dg) > 0:
                                    world.move_hero(hero=world.my_heroes[2], direction=dg[0])
                                    uuu = 1


                elif uuu == 0 and bb == 0 and len(good2) > 0:
                    fff2 = []
                    BB2 = []
                    for gd in good2:
                        if world.manhattan_distance(CEL[2], gd) < 6:
                            bb = 1
                            break
                        else:
                            for cel in M:
                                if world.manhattan_distance(cel, gd) < 6:
                                    fff2.append(cel)
                    if bb == 0 and uuu == 0:
                        for fff in fff2:
                            dg = get_path_move_directions(start_cell=CEL[2], end_cell=fff , world=world)
                            BB2.append(len(dg))
                        if len(BB2) > 0:
                            Y = BB2.index(min(BB2))
                            if (BB2[Y] + FAZ - 1) < 7:
                                dg = get_path_move_directions(start_cell=CEL[2], end_cell=fff2[Y] , world=world)
                                if len(dg) > 0:
                                    world.move_hero(hero=world.my_heroes[2], direction=dg[0])
                                    uuu = 1
                elif uuu == 0 and bb == 0 and len(good1) > 0:
                    fff1 = []
                    BB1 = []
                    for gd in good1:
                        if world.manhattan_distance(CEL[2], gd) < 6:
                            bb = 1
                            break
                        else:
                            for cel in M:
                                if world.manhattan_distance(cel, gd) < 6:
                                    fff1.append(cel)
                    if bb == 0 and uuu == 0:
                        for fff in fff1:
                            dg = get_path_move_directions(start_cell=CEL[2], end_cell=fff , world=world)
                            BB1.append(len(dg))
                        if len(BB1) > 0:
                            Y = BB1.index(min(BB1))
                            if (BB1[Y] + FAZ - 1) < 7:
                                dg = get_path_move_directions(start_cell=CEL[2], end_cell=fff1[Y] , world=world)
                                if len(dg) > 0:
                                    world.move_hero(hero=world.my_heroes[2], direction=dg[0])
                                    uuu = 1
            # if hhh2 is True and  bb == 0 and uuuu==0:
            #     uuuu = 0
            #     if OPCOL[0] != 0 and uuuu == 0:
            #         if world.opp_heroes[0].name == HeroName.BLASTER:
            #             ti = world.opp_heroes[0].get_ability(f).is_ready()
            #             if ti is True:
            #                 if world.manhattan_distance(CEL[2], OPCEL[0]) < 8:
            #                     for cel in M:
            #                         if world.manhattan_distance(start_cell=CEL[2], end_cell=cel) > 2 and cel != CEL[0] and cel != CEL[1] and cel != CEL[3] and uuuu == 0:
            #                             uuuu = 1
            #                             break
            #     if OPCOL[1] != 0 and uuuu == 0:
            #         if world.opp_heroes[1].name == HeroName.BLASTER:
            #             ti = world.opp_heroes[1].get_ability(f).is_ready()
            #             if ti is True:
            #                 if world.manhattan_distance(CEL[2], OPCEL[1]) < 8:
            #                     for cel in M:
            #                         if world.manhattan_distance(start_cell=CEL[2], end_cell=cel) > 2 and cel != CEL[0] and cel != CEL[1] and cel != CEL[3] and uuuu == 0:
            #                             uuuu = 1
            #                             break
            #     if OPCOL[2] != 0 and uuuu == 0:
            #         if world.opp_heroes[2].name == HeroName.BLASTER:
            #             ti = world.opp_heroes[2].get_ability(f).is_ready()
            #             if ti is True:
            #                 if world.manhattan_distance(CEL[2], OPCEL[2]) < 8:
            #                     for cel in M:
            #                         if world.manhattan_distance(start_cell=CEL[2], end_cell=cel) > 2 and cel != CEL[0] and cel != CEL[1] and cel != CEL[3] and uuuu == 0:
            #                             uuuu = 1
            #                             break
            #     if OPCOL[3] != 0 and uuuu == 0:
            #         if world.opp_heroes[3].name == HeroName.BLASTER:
            #             ti = world.opp_heroes[3].get_ability(f).is_ready()
            #             if ti is True:
            #                 if world.manhattan_distance(CEL[2], OPCEL[3]) < 8:
            #                     for cel in M:
            #                         if world.manhattan_distance(start_cell=CEL[2], end_cell=cel) > 2 and cel != CEL[0] and cel != CEL[1] and cel != CEL[3] and uuuu == 0:
            #                             uuuu = 1
            #                             break
            if hh2 is True and uuu == 0 and bb == 0 and l2 != 0 and D == 0 and uuuu==0 and hhh2 is False and h2 is False and world.my_heroes[2].current_hp > 0:
                Q = []
                for cel in M:
                    K = 0
                    if OPCOL[0] != 0:
                        if world.get_impact_cell(ability=world.my_heroes[2].get_ability(fa), start_cell=cel,target_cell=OPCEL[0]) == OPCEL[0]:
                            Q.append(cel)
                            K = 1
                    if OPCOL[1] != 0 and K == 0:
                        if world.get_impact_cell(ability=world.my_heroes[2].get_ability(fa), start_cell=cel,target_cell=OPCEL[1]) == OPCEL[1]:
                            Q.append(cel)
                            K = 1
                    if OPCOL[2] != 0 and K == 0:
                        if world.get_impact_cell(ability=world.my_heroes[2].get_ability(fa), start_cell=cel,target_cell=OPCEL[2]) == OPCEL[2]:
                            Q.append(cel)
                            K = 1
                    if OPCOL[3] != 0 and K == 0:
                        if world.get_impact_cell(ability=world.my_heroes[2].get_ability(fa), start_cell=cel,target_cell=OPCEL[3]) == OPCEL[3]:
                            Q.append(cel)
                            K = 1
                i = 0
                bbbb = []
                bbbb.clear()
                D = 0
                if len(Q) > 0:
                    for q in Q:
                        if q == CEL[2]:
                            D = 1
                            break
                        else:
                            e = get_path_move_directions(start_cell=CEL[2], end_cell=q , world=world)
                            s = len(e)
                            bbbb.append(s)
                    if len(bbbb) > 0:
                        a = bbbb.index(min(bbbb))
                        if D == 0:
                            e = get_path_move_directions(start_cell=CEL[2], end_cell=Q[a] , world=world)
                            if len(e) > 0 and (len(e) + FAZ - 1) < 7:
                                world.move_hero(hero=world.my_heroes[2], direction=e[0])
                                uuu = 1
            # if hhh2 is False and uuu == 0 and bb == 0 and l2 != 0 and D == 0:
            #     i = 0
            #     j = 0
            #     good4 = []
            #     good1 = []
            #     good2 = []
            #     good3 = []
            #     uuu = 0
            #     bb = 0
            #     for cel in M:
            #         j = 0
            #         if OPCOL[0] != 0:
            #             if world.manhattan_distance(cel, OPCEL[0]) > 5:
            #                 j = j + 1
            #         elif OPCOL[0] == 0:
            #             j = j + 1
            #         if OPCOL[1] != 0:
            #             if world.manhattan_distance(cel, OPCEL[1]) > 5:
            #                 j = j + 1
            #         elif OPCOL[1] == 0:
            #             j = j + 1
            #         if OPCOL[2] != 0:
            #             if world.manhattan_distance(cel, OPCEL[2]) > 5:
            #                 j = j + 1
            #         elif OPCOL[2] == 0:
            #             j = j + 1
            #         if OPCOL[3] != 0:
            #             if world.manhattan_distance(cel, OPCEL[3]) > 5:
            #                 j = j + 1
            #         elif OPCOL[3] == 0:
            #             j = j + 1
            #         if j == 4:
            #             good4.append(cel)
            #
            #         elif j == 3:
            #             good3.append(cel)
            #
            #         elif j == 2:
            #             good2.append(cel)
            #
            #         elif j == 1:
            #             good1.append(cel)
            #     if len(good4) != 0:
            #         ff = []
            #         B = []
            #         for gd in good4:
            #             if gd == CEL[2]:
            #                 bb = 1
            #                 break
            #             else:
            #                 ss = world.get_path_move_directions(start_cell=CEL[2], end_cell=gd)
            #                 if (len(ss) + FAZ - 1) < 7:
            #                     ff.append(gd)
            #         if bb == 0 and uuu == 0:
            #             for fff in ff:
            #                 dg = world.get_path_move_directions(start_cell=CEL[2], end_cell=fff)
            #                 B.append(len(dg))
            #             if len(B) > 0:
            #                 Y = B.index(min(B))
            #                 if (B[Y] + FAZ - 1) < 7:
            #                     dg = world.get_path_move_directions(start_cell=CEL[2], end_cell=ff[Y])
            #                     if len(dg) > 0:
            #                         world.move_hero(hero=world.my_heroes[2], direction=dg[0])
            #                         uuu = 1
            #     elif uuu == 0 and bb == 0 and len(good3) > 0:
            #         ff = []
            #         B = []
            #         for gd in good3:
            #             if gd == CEL[2]:
            #                 bb = 1
            #                 break
            #             else:
            #                 ss = world.get_path_move_directions(start_cell=CEL[2], end_cell=gd)
            #                 if (len(ss) + FAZ - 1) < 7:
            #                     ff.append(gd)
            #         if bb == 0 and uuu == 0:
            #             for fff in ff:
            #                 dg = world.get_path_move_directions(start_cell=CEL[2], end_cell=fff)
            #                 B.append(len(dg))
            #             if len(B) > 0:
            #                 Y = B.index(min(B))
            #                 if (B[Y] + FAZ - 1) < 7:
            #                     dg = world.get_path_move_directions(start_cell=CEL[2], end_cell=ff[Y])
            #                     if len(dg) > 0:
            #                         world.move_hero(hero=world.my_heroes[2], direction=dg[0])
            #                         uuu = 1
            #     elif uuu == 0 and bb == 0 and len(good2) > 0:
            #         ff = []
            #         B = []
            #         for gd in good2:
            #             if gd == CEL[2]:
            #                 bb = 1
            #                 break
            #             else:
            #                 ss = world.get_path_move_directions(start_cell=CEL[2], end_cell=gd)
            #                 if (len(ss) + FAZ - 1) < 7:
            #                     ff.append(gd)
            #         if bb == 0 and uuu == 0:
            #             for fff in ff:
            #                 dg = world.get_path_move_directions(start_cell=CEL[2], end_cell=fff)
            #                 B.append(len(dg))
            #             if len(B) > 0:
            #                 Y = B.index(min(B))
            #                 if (B[Y] + FAZ - 1) < 7:
            #                     dg = world.get_path_move_directions(start_cell=CEL[2], end_cell=ff[Y])
            #                     if len(dg) > 0:
            #                         world.move_hero(hero=world.my_heroes[2], direction=dg[0])
            #                         uuu = 1
            #     elif uuu == 0 and bb == 0 and len(good1) > 0:
            #         ff = []
            #         B = []
            #         for gd in good1:
            #             if gd == CEL[2]:
            #                 bb = 1
            #                 break
            #             else:
            #                 ss = world.get_path_move_directions(start_cell=CEL[2], end_cell=gd)
            #                 if (len(ss) + FAZ - 1) < 7:
            #                     ff.append(gd)
            #         if bb == 0 and uuu == 0:
            #             for fff in ff:
            #                 dg = world.get_path_move_directions(start_cell=CEL[2], end_cell=fff)
            #                 B.append(len(dg))
            #             if len(B) > 0:
            #                 Y = B.index(min(B))
            #                 if (B[Y] + FAZ - 1) < 7:
            #                     dg = world.get_path_move_directions(start_cell=CEL[2], end_cell=ff[Y])
            #                     if len(dg) > 0:
            #                         world.move_hero(hero=world.my_heroes[2], direction=dg[0])
            #                         uuu = 1
            if uuu == 0 and bb == 0 and D == 0 and uuuu==0 and world.my_heroes[2].current_hp > 0 and l2==0:
                if len(DO2) > 0:
                    world.move_hero(hero=world.my_heroes[2], direction=DO2[0])
                    uuu = 1
            bb = 0
            uuu = 0
            D = 0
            if h3 is True and uuu == 0 and l3 != 0 and D == 0 and world.my_heroes[3].current_hp > 0 :
                i = 0
                j = 0
                good4 = []
                good1 = []
                good2 = []
                good3 = []
                uuu = 0
                bb = 0
                for cel in N:
                    j = 0
                    if OPCOL[0] != 0:
                        if world.manhattan_distance(cel, OPCEL[0]) < 3:
                            j = j + 1
                    if OPCOL[1] != 0:
                        if world.manhattan_distance(cel, OPCEL[1]) < 3:
                            j = j + 1
                    if OPCOL[2] != 0:
                        if world.manhattan_distance(cel, OPCEL[2]) < 3:
                            j = j + 1
                    if OPCOL[3] != 0:
                        if world.manhattan_distance(cel, OPCEL[3]) < 3:
                            j = j + 1
                    if j == 4:
                        good4.append(cel)

                    elif j == 3:
                        good3.append(cel)

                    elif j == 2:
                        good2.append(cel)

                    elif j == 1:
                        good1.append(cel)
                if len(good4) != 0:
                    ff = []
                    B = []
                    for gd in good4:
                        if world.manhattan_distance(CEL[3], gd) < 6:
                            bb = 1
                            break
                        else:
                            for cel in N:
                                if world.manhattan_distance(cel, gd) < 6:
                                    ff.append(cel)
                    if bb == 0 and uuu == 0:
                        for fff in ff:
                            dg = get_path_move_directions(start_cell=CEL[3], end_cell=fff , world=world)
                            B.append(len(dg))
                        if len(B) > 0:
                            Y = B.index(min(B))
                            if (B[Y] + FAZ - 1) < 7:
                                dg = get_path_move_directions(start_cell=CEL[3], end_cell=ff[Y] , world=world)
                                if len(dg) > 0:
                                    world.move_hero(hero=world.my_heroes[3], direction=dg[0])
                                    uuu = 1

                elif uuu == 0 and bb == 0 and len(good3) > 0:
                    ff = []
                    B = []
                    for gd in good3:
                        if world.manhattan_distance(CEL[3], gd) < 6:
                            bb = 1
                            break
                        else:
                            for cel in N:
                                if world.manhattan_distance(cel, gd) < 6:
                                    ff.append(cel)
                    if bb == 0 and uuu == 0:
                        for fff in ff:
                            dg = get_path_move_directions(start_cell=CEL[3], end_cell=fff , world=world)
                            B.append(len(dg))
                        if len(B) > 0:
                            Y = B.index(min(B))
                            if (B[Y] + FAZ - 1) < 7:
                                dg = get_path_move_directions(start_cell=CEL[3], end_cell=ff[Y] , world=world)
                                if len(dg) > 0:
                                    world.move_hero(hero=world.my_heroes[3], direction=dg[0])
                                    uuu = 1

                elif uuu == 0 and bb == 0 and len(good2) > 0:
                    fff2 = []
                    BB2 = []
                    for gd in good2:
                        if world.manhattan_distance(CEL[3], gd) < 6:
                            bb = 1
                            break
                        else:
                            for cel in N:
                                if world.manhattan_distance(cel, gd) < 6:
                                    fff2.append(cel)
                    if bb == 0 and uuu == 0:
                        for fff in fff2:
                            dg = get_path_move_directions(start_cell=CEL[3], end_cell=fff ,world=world)
                            BB2.append(len(dg))
                        if len(BB2) > 0:
                            Y = BB2.index(min(BB2))
                            if (BB2[Y] + FAZ - 1) < 7:
                                dg = get_path_move_directions(start_cell=CEL[3], end_cell=fff2[Y] , world=world)
                                if len(dg) > 0:
                                    world.move_hero(hero=world.my_heroes[3], direction=dg[0])
                                    uuu = 1

                elif uuu == 0 and bb == 0 and len(good1) > 0:
                    fffW = []
                    BBW = []
                    for gd in good1:
                        if world.manhattan_distance(CEL[3], gd) < 6:
                            bb = 1
                            break
                        else:
                            for cel in N:
                                if world.manhattan_distance(cel, gd) < 6:
                                    fffW.append(cel)
                    if bb == 0 and uuu == 0:
                        for fffff in fffW:
                            dg = get_path_move_directions(start_cell=CEL[3], end_cell=fffff ,world=world)
                            BBW.append(len(dg))
                        if len(BBW) > 0:
                            Y = BBW.index(min(BBW))
                            if (BBW[Y] + FAZ - 1) < 7:
                                dg = get_path_move_directions(start_cell=CEL[3], end_cell=fffW[Y] , world=world)
                                if len(dg) > 0:
                                    world.move_hero(hero=world.my_heroes[3], direction=dg[0])
                                    uuu = 1
            # if hhh3 is True and bb == 0 and uuuu==0:
            #     uuuu = 0
            #     if OPCOL[0] != 0 and uuuu == 0:
            #         if world.opp_heroes[0].name == HeroName.BLASTER:
            #             ti = world.opp_heroes[0].get_ability(f).is_ready()
            #             if ti is True:
            #                 if world.manhattan_distance(CEL[3], OPCEL[0]) < 8:
            #                     for cel in N:
            #                         if world.manhattan_distance(start_cell=CEL[3], end_cell=cel) > 2 and cel != CEL[0] and cel != CEL[1] and cel != CEL[2] and uuuu == 0:
            #                             uuuu = 1
            #                             break
            #     if OPCOL[1] != 0 and uuuu == 0:
            #         if world.opp_heroes[1].name == HeroName.BLASTER:
            #             ti = world.opp_heroes[1].get_ability(f).is_ready()
            #             if ti is True:
            #                 if world.manhattan_distance(CEL[3], OPCEL[1]) < 8:
            #                     for cel in N:
            #                         if world.manhattan_distance(start_cell=CEL[3], end_cell=cel) > 2 and cel != CEL[0] and cel != CEL[1] and cel != CEL[2] and uuuu == 0:
            #                             uuuu = 1
            #                             break
            #     if OPCOL[2] != 0 and uuuu == 0:
            #         if world.opp_heroes[2].name == HeroName.BLASTER:
            #             ti = world.opp_heroes[2].get_ability(f).is_ready()
            #             if ti is True:
            #                 if world.manhattan_distance(CEL[3], OPCEL[2]) < 8:
            #                     for cel in N:
            #                         if world.manhattan_distance(start_cell=CEL[3], end_cell=cel) > 2 and cel != CEL[0] and cel != CEL[1] and cel != CEL[2] and uuuu == 0:
            #                             uuuu = 1
            #                             break
            #     if OPCOL[3] != 0 and uuuu == 0:
            #         if world.opp_heroes[3].name == HeroName.BLASTER:
            #             ti = world.opp_heroes[3].get_ability(f).is_ready()
            #             if ti is True:
            #                 if world.manhattan_distance(CEL[3], OPCEL[3]) < 8:
            #                     for cel in N:
            #                         if world.manhattan_distance(start_cell=CEL[3], end_cell=cel) > 2 and cel != CEL[0] and cel != CEL[1] and cel != CEL[2] and uuuu == 0:
            #                             uuuu = 1
            #                             break
            if hh3 is True and uuu == 0 and bb == 0 and l3 != 0 and D == 0 and uuuu==0 and hhh3 is False and h3 is False and world.my_heroes[3].current_hp > 0:
                Q = []
                for cel in N:
                    K = 0
                    if OPCOL[0] != 0:
                        if world.get_impact_cell(ability=world.my_heroes[3].get_ability(fa), start_cell=cel,target_cell=OPCEL[0]) == OPCEL[0]:
                            Q.append(cel)
                            K = 1
                    if OPCOL[1] != 0 and K == 0:
                        if world.get_impact_cell(ability=world.my_heroes[3].get_ability(fa), start_cell=cel,target_cell=OPCEL[1]) == OPCEL[1]:
                            Q.append(cel)
                            K = 1
                    if OPCOL[2] != 0 and K == 0:
                        if world.get_impact_cell(ability=world.my_heroes[3].get_ability(fa), start_cell=cel,target_cell=OPCEL[2]) == OPCEL[2]:
                            Q.append(cel)
                            K = 1
                    if OPCOL[3] != 0 and K == 0:
                        if world.get_impact_cell(ability=world.my_heroes[3].get_ability(fa), start_cell=cel,target_cell=OPCEL[3]) == OPCEL[3]:
                            Q.append(cel)
                            K = 1
                i = 0
                bbbb = []
                bbbb.clear()
                D = 0
                if len(Q) > 0:
                    for q in Q:
                        if q == CEL[3]:
                            D = 1
                            break
                        else:
                            e = get_path_move_directions(start_cell=CEL[3], end_cell=q ,world=world)
                            s = len(e)
                            bbbb.append(s)
                    if len(bbbb) > 0:
                        a = bbbb.index(min(bbbb))
                        if D == 0:
                            e = get_path_move_directions(start_cell=CEL[3], end_cell=Q[a] , world=world)
                            if len(e) > 0 and (len(e) + FAZ - 1) < 7:
                                world.move_hero(hero=world.my_heroes[3], direction=e[0])
                                uuu = 1
            # if hhh3 is False and uuu == 0 and bb == 0 and l3 != 0 and D == 0:
            #     i = 0
            #     j = 0
            #     good4 = []
            #     good1 = []
            #     good2 = []
            #     good3 = []
            #     uuu = 0
            #     bb = 0
            #     for cel in N:
            #         j = 0
            #         if OPCOL[0] != 0:
            #             if world.manhattan_distance(cel, OPCEL[0]) > 5:
            #                 j = j + 1
            #         elif OPCOL[0] == 0:
            #             j = j + 1
            #         if OPCOL[1] != 0:
            #             if world.manhattan_distance(cel, OPCEL[1]) > 5:
            #                 j = j + 1
            #         elif OPCOL[1] == 0:
            #             j = j + 1
            #         if OPCOL[2] != 0:
            #             if world.manhattan_distance(cel, OPCEL[2]) > 5:
            #                 j = j + 1
            #         elif OPCOL[2] == 0:
            #             j = j + 1
            #         if OPCOL[3] != 0:
            #             if world.manhattan_distance(cel, OPCEL[3]) > 5:
            #                 j = j + 1
            #         elif OPCOL[3] == 0:
            #             j = j + 1
            #         if j == 4:
            #             good4.append(cel)
            #
            #         elif j == 3:
            #             good3.append(cel)
            #
            #         elif j == 2:
            #             good2.append(cel)
            #
            #         elif j == 1:
            #             good1.append(cel)
            #     if len(good4) != 0:
            #         ff = []
            #         B = []
            #         for gd in good4:
            #             if gd == CEL[3]:
            #                 bb = 1
            #                 break
            #             else:
            #                 ss = world.get_path_move_directions(start_cell=CEL[3], end_cell=gd)
            #                 if (len(ss) + FAZ - 1) < 7:
            #                     ff.append(gd)
            #         if bb == 0 and uuu == 0:
            #             for fff in ff:
            #                 dg = world.get_path_move_directions(start_cell=CEL[3], end_cell=fff)
            #                 B.append(len(dg))
            #             if len(B) > 0:
            #                 Y = B.index(min(B))
            #                 if (B[Y] + FAZ - 1) < 7:
            #                     dg = world.get_path_move_directions(start_cell=CEL[3], end_cell=ff[Y])
            #                     if len(dg) > 0:
            #                         world.move_hero(hero=world.my_heroes[3], direction=dg[0])
            #                         uuu = 1
            #
            #     elif uuu == 0 and bb == 0 and len(good3) > 0:
            #         ff = []
            #         B = []
            #         for gd in good3:
            #             if gd == CEL[3]:
            #                 bb = 1
            #                 break
            #             else:
            #                 ss = world.get_path_move_directions(start_cell=CEL[3], end_cell=gd)
            #                 if (len(ss) + FAZ - 1) < 7:
            #                     ff.append(gd)
            #         if bb == 0 and uuu == 0:
            #             for fff in ff:
            #                 dg = world.get_path_move_directions(start_cell=CEL[3], end_cell=fff)
            #                 B.append(len(dg))
            #             if len(B) > 0:
            #                 Y = B.index(min(B))
            #                 if (B[Y] + FAZ - 1) < 7:
            #                     dg = world.get_path_move_directions(start_cell=CEL[3], end_cell=ff[Y])
            #                     if len(dg) > 0:
            #                         world.move_hero(hero=world.my_heroes[3], direction=dg[0])
            #                         uuu = 1
            #
            #     elif uuu == 0 and bb == 0 and len(good2) > 0:
            #         ff = []
            #         B = []
            #         for gd in good2:
            #             if gd == CEL[3]:
            #                 bb = 1
            #                 break
            #             else:
            #                 ss = world.get_path_move_directions(start_cell=CEL[3], end_cell=gd)
            #                 if (len(ss) + FAZ - 1) < 7:
            #                     ff.append(gd)
            #         if bb == 0 and uuu == 0:
            #             for fff in ff:
            #                 dg = world.get_path_move_directions(start_cell=CEL[3], end_cell=fff)
            #                 B.append(len(dg))
            #             if len(B) > 0:
            #                 Y = B.index(min(B))
            #                 if (B[Y] + FAZ - 1) < 7:
            #                     dg = world.get_path_move_directions(start_cell=CEL[3], end_cell=ff[Y])
            #                     if len(dg) > 0:
            #                         world.move_hero(hero=world.my_heroes[3], direction=dg[0])
            #                         uuu = 1
            #
            #     elif uuu == 0 and bb == 0 and len(good1) > 0:
            #         ff = []
            #         B = []
            #         for gd in good1:
            #             if gd == CEL[3]:
            #                 bb = 1
            #                 break
            #             else:
            #                 ss = world.get_path_move_directions(start_cell=CEL[3], end_cell=gd)
            #                 if (len(ss) + FAZ - 1) < 7:
            #                     ff.append(gd)
            #         if bb == 0 and uuu == 0:
            #             for fff in ff:
            #                 dg = world.get_path_move_directions(start_cell=CEL[3], end_cell=fff)
            #                 B.append(len(dg))
            #             if len(B) > 0:
            #                 Y = B.index(min(B))
            #                 if (B[Y] + FAZ - 1) < 7:
            #                     dg = world.get_path_move_directions(start_cell=CEL[3], end_cell=ff[Y])
            #                     if len(dg) > 0:
            #                         world.move_hero(hero=world.my_heroes[3], direction=dg[0])
            #                         uuu = 1
            if uuu == 0 and bb == 0 and D == 0 and uuuu==0 and world.my_heroes[3].current_hp > 0 and l3==0:
                if len(DO3) > 0:
                    world.move_hero(hero=world.my_heroes[3], direction=DO3[0])
                    uuu = 1
        else:
            bb = 0
            uuu = 0
            D = 0
            uuuu=0
            if h1 is True and uuu == 0 and l1 != 0 and D == 0 and FAZ>5 and world.my_heroes[1].current_hp > 0:
                good4 = []
                good1 = []
                good2 = []
                good3 = []
                uuu = 0
                bb = 0
                for cel in H:
                    j = 0
                    if OPCOL[0] != 0:
                        if world.manhattan_distance(start_cell=cel, end_cell=OPCEL[0]) < 3:
                            j = j + 1
                    if OPCOL[1] != 0:
                        if world.manhattan_distance(start_cell=cel, end_cell=OPCEL[1]) < 3:
                            j = j + 1
                    if OPCOL[2] != 0:
                        if world.manhattan_distance(start_cell=cel, end_cell=OPCEL[2]) < 3:
                            j = j + 1
                    if OPCOL[3] != 0:
                        if world.manhattan_distance(start_cell=cel, end_cell=OPCEL[3]) < 3:
                            j = j + 1
                    if j == 4:
                        good4.append(cel)

                    elif j == 3:
                        good3.append(cel)

                    elif j == 2:
                        good2.append(cel)

                    elif j == 1:
                        good1.append(cel)
                if len(good4) > 0:
                    ff = []
                    B = []
                    for gd in good4:
                        ff = []
                        B = []
                        if world.manhattan_distance(start_cell=CEL[1], end_cell=gd) < 6:
                            bb = 1
                            break
                        elif uuu == 0 and bb == 0:
                            ff = []
                            B = []
                            for cel in H:
                                if world.manhattan_distance(cel, gd) < 6:
                                    ff.append(cel)
                    if bb == 0:
                        for fff in ff:
                            dg = get_path_move_directions(start_cell=CEL[1], end_cell=fff, world=world)
                            B.append(len(dg))
                        if len(B) > 0:
                            Y = B.index(min(B))
                            if (B[Y] + FAZ - 1) < 7 and bb == 0:
                                dg = get_path_move_directions(start_cell=CEL[1], end_cell=ff[Y], world=world)
                                if len(dg) > 0:
                                    world.move_hero(hero=world.my_heroes[1], direction=dg[0])
                                    uuu = 1
                elif uuu == 0 and bb == 0 and len(good3) > 0:
                    ff = []
                    B = []
                    for gd in good3:
                        ff = []
                        B = []
                        if world.manhattan_distance(CEL[1], gd) < 6:
                            bb = 1
                            break
                        elif uuu == 0 and bb == 0:
                            ff = []
                            B = []
                            for cel in H:
                                if world.manhattan_distance(cel, gd) < 6:
                                    ff.append(cel)
                    if bb == 0:
                        for fff in ff:
                            dg = get_path_move_directions(start_cell=CEL[1], end_cell=fff, world=world)
                            B.append(len(dg))
                        if len(B) > 0:
                            Y = B.index(min(B))
                            if (B[Y] + FAZ - 1) < 7:
                                dg = get_path_move_directions(start_cell=CEL[1], end_cell=ff[Y], world=world)
                                if len(dg) > 0:
                                    world.move_hero(hero=world.my_heroes[1], direction=dg[0])
                                    uuu = 1
                elif uuu == 0 and bb == 0 and len(good2) > 0:
                    fff2 = []
                    BB2 = []
                    for gd in good2:
                        fff2 = []
                        BB2 = []
                        if world.manhattan_distance(CEL[1], gd) < 6:
                            bb = 1
                            break
                        elif uuu == 0 and bb == 0:
                            fff2 = []
                            BB2 = []
                            for cel in H:
                                if world.manhattan_distance(cel, gd) < 6:
                                    fff2.append(cel)
                    if bb == 0:
                        for fff in fff2:
                            dg = get_path_move_directions(start_cell=CEL[1], end_cell=fff, world=world)
                            BB2.append(len(dg))
                        if len(BB2) > 0:
                            Y = BB2.index(min(BB2))
                            if (BB2[Y] + FAZ - 1) < 7:
                                dg = get_path_move_directions(start_cell=CEL[1], end_cell=fff2[Y], world=world)
                                if len(dg) > 0:
                                    world.move_hero(hero=world.my_heroes[1], direction=dg[0])
                                    uuu = 1
                elif uuu == 0 and bb == 0 and len(good1) > 0:
                    fff1 = []
                    BB1 = []
                    for gd in good1:
                        fff1 = []
                        BB1 = []
                        if world.manhattan_distance(CEL[1], gd) < 6:
                            bb = 1
                            break
                        elif uuu == 0 and bb == 0:
                            fff1 = []
                            BB1 = []
                            for cel in H:
                                if world.manhattan_distance(cel, gd) < 6:
                                    fff1.append(cel)
                    if bb == 0:
                        for fff in fff1:
                            dg = get_path_move_directions(start_cell=CEL[1], end_cell=fff, world=world)
                            BB1.append(len(dg))
                        if len(BB1) > 0:
                            Y = BB1.index(min(BB1))
                            if (BB1[Y] + FAZ - 1) < 7:
                                dg = get_path_move_directions(start_cell=CEL[1], end_cell=fff1[Y], world=world)
                                if len(dg) > 0:
                                    world.move_hero(hero=world.my_heroes[1], direction=dg[0])
                                    uuu = 1
            # if hhh1 is True and  bb == 0 and uuuu==0:
            #     uuuu = 0
            #     if OPCOL[0] != 0 and uuuu == 0:
            #         if world.opp_heroes[0].name == HeroName.BLASTER:
            #             ti = world.opp_heroes[0].get_ability(f).is_ready()
            #             if ti is True:
            #                 if world.manhattan_distance(CEL[1], OPCEL[0]) < 8:
            #                     for cel in H:
            #                         if world.manhattan_distance(start_cell=CEL[1], end_cell=cel) > 2 and cel != CEL[0] and cel != CEL[2] and cel != CEL[3] and uuuu == 0:
            #                             uuuu = 1
            #                             break
            #     if OPCOL[1] != 0 and uuuu == 0:
            #         if world.opp_heroes[1].name == HeroName.BLASTER:
            #             ti = world.opp_heroes[1].get_ability(f).is_ready()
            #             if ti is True:
            #                 if world.manhattan_distance(CEL[1], OPCEL[1]) < 8:
            #                     for cel in H:
            #                         if world.manhattan_distance(start_cell=CEL[1], end_cell=cel) > 2 and cel != CEL[0] and cel != CEL[2] and cel != CEL[3] and uuuu == 0:
            #                             uuuu = 1
            #                             break
            #     if OPCOL[2] != 0 and uuuu == 0:
            #         if world.opp_heroes[2].name == HeroName.BLASTER:
            #             ti = world.opp_heroes[2].get_ability(f).is_ready()
            #             if ti is True:
            #                 if world.manhattan_distance(CEL[1], OPCEL[2]) < 8:
            #                     for cel in H:
            #                         if world.manhattan_distance(start_cell=CEL[1], end_cell=cel) > 2 and cel != CEL[0] and cel != CEL[2] and cel != CEL[3] and uuuu == 0:
            #                             uuuu = 1
            #                             break
            #     if OPCOL[3] != 0 and uuuu == 0:
            #         if world.opp_heroes[3].name == HeroName.BLASTER:
            #             ti = world.opp_heroes[3].get_ability(f).is_ready()
            #             if ti is True:
            #                 if world.manhattan_distance(CEL[1], OPCEL[3]) < 8:
            #                     for cel in H:
            #                         if world.manhattan_distance(start_cell=CEL[1], end_cell=cel) > 2 and cel != CEL[0] and cel != CEL[2] and cel != CEL[3] and uuuu == 0:
            #                             uuuu = 1
            #                             break
            if hh1 is True and uuu == 0 and bb == 0 and l1 != 0 and D == 0 and h1 is False and FAZ>4 and hhh1 is False and uuuu==0 and world.my_heroes[1].current_hp > 0:
                Q = []
                for cel in H:
                    K = 0
                    if OPCOL[0] != 0:
                        if world.get_impact_cell(ability=world.my_heroes[1].get_ability(fa), start_cell=cel,target_cell=OPCEL[0]) == OPCEL[0]:
                            Q.append(cel)
                            K = 1
                    if OPCOL[1] != 0 and K == 0:
                        if world.get_impact_cell(ability=world.my_heroes[1].get_ability(fa), start_cell=cel,target_cell=OPCEL[1]) == OPCEL[1]:
                            Q.append(cel)
                            K = 1
                    if OPCOL[2] != 0 and K == 0:
                        if world.get_impact_cell(ability=world.my_heroes[1].get_ability(fa), start_cell=cel,target_cell=OPCEL[2]) == OPCEL[2]:
                            Q.append(cel)
                            K = 1
                    if OPCOL[3] != 0 and K == 0:
                        if world.get_impact_cell(ability=world.my_heroes[1].get_ability(fa), start_cell=cel,target_cell=OPCEL[3]) == OPCEL[3]:
                            Q.append(cel)
                            K = 1
                i = 0
                bbbb = []
                ww = 1000
                bbbb.clear()
                D = 0
                if len(Q) > 0:
                    for q in Q:
                        if q == CEL[1]:
                            D = 1
                            break
                        else:
                            e = get_path_move_directions(start_cell=CEL[1], end_cell=q, world=world)
                            s = len(e)
                            bbbb.append(s)
                    if len(bbbb) > 0:
                        a = bbbb.index(min(bbbb))
                        if D == 0:
                            e = get_path_move_directions(start_cell=CEL[1], end_cell=Q[a], world=world)
                            if len(e) > 0 and (len(e) + FAZ - 1) < 7:
                                world.move_hero(hero=world.my_heroes[1], direction=e[0])
                                uuu = 1
            # if hhh1 is False and uuu == 0 and bb == 0 and l1 != 0 and D == 0 and h1 is False and hh1 is False:
            #     i = 0
            #     j = 0
            #     good4 = []
            #     good1 = []
            #     good2 = []
            #     good3 = []
            #     good = []
            #     uuu = 0
            #     bb = 0
            #     for cel in H:
            #         j = 0
            #         if OPCOL[0] != 0:
            #             if world.manhattan_distance(cel, OPCEL[0]) > 5:
            #                 j = j + 1
            #         elif OPCOL[0] == 0:
            #             j = j + 1
            #         if OPCOL[1] != 0:
            #             if world.manhattan_distance(cel, OPCEL[1]) > 5:
            #                 j = j + 1
            #         elif OPCOL[1] == 0:
            #             j = j + 1
            #         if OPCOL[2] != 0:
            #             if world.manhattan_distance(cel, OPCEL[2]) > 5:
            #                 j = j + 1
            #         elif OPCOL[2] == 0:
            #             j = j + 1
            #         if OPCOL[3] != 0:
            #             if world.manhattan_distance(cel, OPCEL[3]) > 5:
            #                 j = j + 1
            #         elif OPCOL[3] == 0:
            #             j = j + 1
            #         if j == 4:
            #             good4.append(cel)
            #
            #         elif j == 3:
            #             good3.append(cel)
            #
            #         elif j == 2:
            #             good2.append(cel)
            #
            #         elif j == 1:
            #             good1.append(cel)
            #     if len(good4) != 0:
            #         ff = []
            #         B = []
            #         for gd in good4:
            #             if gd == CEL[1]:
            #                 bb = 1
            #                 break
            #             else:
            #                 ss = world.get_path_move_directions(start_cell=CEL[1], end_cell=gd)
            #                 if (len(ss) + FAZ - 1) < 7:
            #                     ff.append(gd)
            #         if bb == 0 and len(ff) > 0:
            #             for fff in ff:
            #                 dg = world.get_path_move_directions(start_cell=CEL[1], end_cell=fff)
            #                 B.append(len(dg))
            #             if len(B) > 0:
            #                 Y = B.index(min(B))
            #                 if (B[Y] + FAZ - 1) < 7:
            #                     dg = world.get_path_move_directions(start_cell=CEL[1], end_cell=ff[Y])
            #                     if len(dg) > 0:
            #                         world.move_hero(hero=world.my_heroes[1], direction=dg[0])
            #                         uuu = 1
            #
            #
            #     elif uuu == 0 and bb == 0 and len(good3) > 0:
            #         ff = []
            #         B = []
            #         for gd in good3:
            #             if gd == CEL[1]:
            #                 bb = 1
            #                 break
            #             else:
            #                 ss = world.get_path_move_directions(start_cell=CEL[1], end_cell=gd)
            #                 if (len(ss) + FAZ - 1) < 7:
            #                     ff.append(gd)
            #         if bb == 0 and len(ff) > 0:
            #             for fff in ff:
            #                 dg = world.get_path_move_directions(start_cell=CEL[1], end_cell=fff)
            #                 B.append(len(dg))
            #             if len(B) > 0:
            #                 Y = B.index(min(B))
            #                 if (B[Y] + FAZ - 1) < 7:
            #                     dg = world.get_path_move_directions(start_cell=CEL[1], end_cell=ff[Y])
            #                     if len(dg) > 0:
            #                         world.move_hero(hero=world.my_heroes[1], direction=dg[0])
            #                         uuu = 1
            #
            #
            #     elif uuu == 0 and bb == 0 and len(good2) > 0:
            #         ff = []
            #         B = []
            #         for gd in good2:
            #             if gd == CEL[1]:
            #                 bb = 1
            #                 break
            #             else:
            #                 ss = world.get_path_move_directions(start_cell=CEL[1], end_cell=gd)
            #                 if (len(ss) + FAZ - 1) < 7:
            #                     ff.append(gd)
            #         if bb == 0 and len(ff) > 0:
            #             for fff in ff:
            #                 dg = world.get_path_move_directions(start_cell=CEL[1], end_cell=fff)
            #                 B.append(len(dg))
            #             if len(B) > 0:
            #                 Y = B.index(min(B))
            #                 if (B[Y] + FAZ - 1) < 7:
            #                     dg = world.get_path_move_directions(start_cell=CEL[1], end_cell=ff[Y])
            #                     if len(dg) > 0:
            #                         world.move_hero(hero=world.my_heroes[1], direction=dg[0])
            #                         uuu = 1
            #
            #
            #     elif uuu == 0 and bb == 0 and len(good1) > 0:
            #         ff = []
            #         B = []
            #         for gd in good1:
            #             if gd == CEL[1]:
            #                 bb = 1
            #                 break
            #             else:
            #                 ss = world.get_path_move_directions(start_cell=CEL[1], end_cell=gd)
            #                 if (len(ss) + FAZ - 1) < 7:
            #                     ff.append(gd)
            #         if bb == 0 and len(ff) > 0:
            #             for fff in ff:
            #                 dg = world.get_path_move_directions(start_cell=CEL[1], end_cell=fff)
            #                 B.append(len(dg))
            #             if len(B) > 0:
            #                 Y = B.index(min(B))
            #                 if (B[Y] + FAZ - 1) < 7:
            #                     dg = world.get_path_move_directions(start_cell=CEL[1], end_cell=ff[Y])
            #                     if len(dg) > 0:
            #                         world.move_hero(hero=world.my_heroes[1], direction=dg[0])
            #                         uuu = 1
            if uuu == 0 and bb == 0 and D == 0 and l1 ==0 and uuuu==0 and world.my_heroes[1].current_hp > 0 and l1==0:
                if len(DO1) > 0:
                    world.move_hero(hero=world.my_heroes[1], direction=DO1[0])
                    uuu = 1
            uuu = 0
            bb = 0
            D = 0
            if h is True and uuu == 0 and l != 0 and D == 0 and FAZ>5 and world.my_heroes[0].current_hp > 0:
                i = 0
                j = 0
                good4 = []
                good1 = []
                good2 = []
                good3 = []
                uuu = 0
                bb = 0
                for cel in G:
                    j = 0
                    if OPCOL[0] != 0:
                        if world.manhattan_distance(cel, OPCEL[0]) < 3:
                            j = j + 1
                    if OPCOL[1] != 0:
                        if world.manhattan_distance(cel, OPCEL[1]) < 3:
                            j = j + 1
                    if OPCOL[2] != 0:
                        if world.manhattan_distance(cel, OPCEL[2]) < 3:
                            j = j + 1
                    if OPCOL[3] != 0:
                        if world.manhattan_distance(cel, OPCEL[3]) < 3:
                            j = j + 1
                    if j == 4:
                        good4.append(cel)

                    elif j == 3:
                        good3.append(cel)

                    elif j == 2:
                        good2.append(cel)

                    elif j == 1:
                        good1.append(cel)
                if len(good4) != 0:
                    ff = []
                    B = []
                    for gd in good4:
                        if world.manhattan_distance(CEL[0], gd) < 6:
                            bb = 1
                            break
                        else:
                            for cel in G:
                                if world.manhattan_distance(cel, gd) < 6:
                                    ff.append(cel)
                    if bb == 0 and uuu == 0:
                        for fff in ff:
                            dg = get_path_move_directions(start_cell=CEL[0], end_cell=fff, world=world)
                            B.append(len(dg))
                        if len(B) > 0:
                            Y = B.index(min(B))
                            if (B[Y] + FAZ - 1) < 7:
                                dg = get_path_move_directions(start_cell=CEL[0], end_cell=ff[Y], world=world)
                                if len(dg) > 0:
                                    world.move_hero(hero=world.my_heroes[0], direction=dg[0])
                                    uuu = 1

                elif uuu == 0 and bb == 0 and len(good3) > 0:
                    ff = []
                    B = []
                    for gd in good3:
                        if world.manhattan_distance(CEL[0], gd) < 6:
                            bb = 1
                            break
                        else:
                            for cel in G:
                                if world.manhattan_distance(cel, gd) < 6:
                                    ff.append(cel)
                    if bb == 0 and uuu == 0:
                        for fff in ff:
                            dg = get_path_move_directions(start_cell=CEL[0], end_cell=fff, world=world)
                            B.append(len(dg))
                        if len(B) > 0:
                            Y = B.index(min(B))
                            if (B[Y] + FAZ - 1) < 7:
                                dg = get_path_move_directions(start_cell=CEL[0], end_cell=ff[Y], world=world)
                                if len(dg) > 0:
                                    world.move_hero(hero=world.my_heroes[0], direction=dg[0])
                                    uuu = 1
                elif uuu == 0 and bb == 0 and len(good2) > 0:
                    fff2 = []
                    BB2 = []
                    for gd in good2:
                        if world.manhattan_distance(CEL[0], gd) < 6:
                            bb = 1
                            break
                        else:
                            for cel in G:
                                if world.manhattan_distance(cel, gd) < 6:
                                    fff2.append(cel)
                    if bb == 0 and uuu == 0:
                        for fff in fff2:
                            dg = get_path_move_directions(start_cell=CEL[0], end_cell=fff, world=world)
                            BB2.append(len(dg))
                        if len(BB2) > 0:
                            Y = BB2.index(min(BB2))
                            if (BB2[Y] + FAZ - 1) < 7:
                                dg = get_path_move_directions(start_cell=CEL[0], end_cell=fff2[Y], world=world)
                                if len(dg) > 0:
                                    world.move_hero(hero=world.my_heroes[0], direction=dg[0])
                                    uuu = 1


                elif uuu == 0 and bb == 0 and len(good1) > 0:
                    fff1 = []
                    BB1 = []
                    for gd in good1:
                        if world.manhattan_distance(CEL[0], gd) < 6:
                            bb = 1
                            break
                        else:
                            for cel in G:
                                if world.manhattan_distance(cel, gd) < 6:
                                    fff1.append(cel)
                    if bb == 0 and uuu == 0:
                        for fff in fff1:
                            dg = get_path_move_directions(start_cell=CEL[0], end_cell=fff, world=world)
                            BB1.append(len(dg))
                        if len(BB1) > 0:
                            Y = BB1.index(min(BB1))
                            if (BB1[Y] + FAZ - 1) < 7:
                                dg = get_path_move_directions(start_cell=CEL[0], end_cell=fff1[Y], world=world)
                                if len(dg) > 0:
                                    world.move_hero(hero=world.my_heroes[0], direction=dg[0])
                                    uuu = 1
            # if hhh is True and bb == 0 and uuuu == 0:
            #     uuuu = 0
            #     if OPCOL[0] != 0 and uuuu == 0:
            #         if world.opp_heroes[0].name == HeroName.BLASTER:
            #             ti = world.opp_heroes[0].get_ability(f).is_ready()
            #             if ti is True:
            #                 if world.manhattan_distance(CEL[0], OPCEL[0]) < 8:
            #                     for cel in G:
            #                         if world.manhattan_distance(start_cell=CEL[0], end_cell=cel) > 2 and cel != CEL[
            #                             1] and cel != CEL[2] and cel != CEL[3] and uuuu == 0:
            #                             uuuu = 1
            #                             break
            #     if OPCOL[1] != 0 and uuuu == 0:
            #         if world.opp_heroes[1].name == HeroName.BLASTER:
            #             ti = world.opp_heroes[1].get_ability(f).is_ready()
            #             if ti is True:
            #                 if world.manhattan_distance(CEL[0], OPCEL[1]) < 8:
            #                     for cel in G:
            #                         if world.manhattan_distance(start_cell=CEL[0], end_cell=cel) > 2 and cel != CEL[
            #                             1] and cel != CEL[2] and cel != CEL[3] and uuuu == 0:
            #                             uuuu = 1
            #                             break
            #     if OPCOL[2] != 0 and uuuu == 0:
            #         if world.opp_heroes[2].name == HeroName.BLASTER:
            #             ti = world.opp_heroes[2].get_ability(f).is_ready()
            #             if ti is True:
            #                 if world.manhattan_distance(CEL[0], OPCEL[2]) < 8:
            #                     for cel in G:
            #                         if world.manhattan_distance(start_cell=CEL[0], end_cell=cel) > 2 and cel != CEL[
            #                             1] and cel != CEL[2] and cel != CEL[3] and uuuu == 0:
            #                             uuuu = 1
            #                             break
            #     if OPCOL[3] != 0 and uuuu == 0:
            #         if world.opp_heroes[3].name == HeroName.BLASTER:
            #             ti = world.opp_heroes[3].get_ability(f).is_ready()
            #             if ti is True:
            #                 if world.manhattan_distance(CEL[0], OPCEL[3]) < 8:
            #                     for cel in G:
            #                         if world.manhattan_distance(start_cell=CEL[0], end_cell=cel) > 2 and cel != CEL[
            #                             1] and cel != CEL[2] and cel != CEL[3] and uuuu == 0:
            #                             uuuu = 1
            #                             break
            if hh is True and uuu == 0 and bb == 0 and l != 0 and D == 0 and h is False and FAZ>4 and hhh is False and uuuu==0 and world.my_heroes[0].current_hp > 0:
                Q = []
                for cel in G:
                    K = 0
                    if OPCOL[0] != 0:
                        if world.get_impact_cell(ability=world.my_heroes[0].get_ability(fa), start_cell=cel,target_cell=OPCEL[0]) == OPCEL[0]:
                            Q.append(cel)
                            K = 1
                    if OPCOL[1] != 0 and K == 0:
                        if world.get_impact_cell(ability=world.my_heroes[0].get_ability(fa), start_cell=cel,target_cell=OPCEL[1]) == OPCEL[1]:
                            Q.append(cel)
                            K = 1
                    if OPCOL[2] != 0 and K == 0:
                        if world.get_impact_cell(ability=world.my_heroes[0].get_ability(fa), start_cell=cel,target_cell=OPCEL[2]) == OPCEL[2]:
                            Q.append(cel)
                            K = 1
                    if OPCOL[3] != 0 and K == 0:
                        if world.get_impact_cell(ability=world.my_heroes[0].get_ability(fa), start_cell=cel,target_cell=OPCEL[3]) == OPCEL[3]:
                            Q.append(cel)
                            K = 1
                i = 0
                bbbb = []
                bbbb.clear()
                D = 0
                if len(Q) > 0:
                    for q in Q:
                        if q == CEL[0]:
                            D = 1
                            break
                        else:
                            e = get_path_move_directions(start_cell=CEL[0], end_cell=q, world=world)
                            s = len(e)
                            bbbb.append(s)
                    if len(bbbb) > 0:
                        a = bbbb.index(min(bbbb))
                        if D == 0:
                            e = get_path_move_directions(start_cell=CEL[0], end_cell=Q[a], world=world)
                            if len(e) > 0 and (len(e) + FAZ - 1) < 7:
                                world.move_hero(hero=world.my_heroes[0], direction=e[0])
                                uuu = 1
            # if hhh is False and uuu == 0 and bb == 0 and l != 0 and D == 0 and h is False and hh is False:
            #     i = 0
            #     j = 0
            #     good4 = []
            #     good1 = []
            #     good2 = []
            #     good3 = []
            #     uuu = 0
            #     bb = 0
            #     for cel in G:
            #         j = 0
            #         if OPCOL[0] != 0:
            #             if world.manhattan_distance(cel, OPCEL[0]) > 5:
            #                 j = j + 1
            #         elif OPCOL[0] == 0:
            #             j = j + 1
            #
            #         if OPCOL[1] != 0:
            #             if world.manhattan_distance(cel, OPCEL[1]) > 5:
            #                 j = j + 1
            #         elif OPCOL[1] == 0:
            #             j = j + 1
            #         if OPCOL[2] != 0:
            #             if world.manhattan_distance(cel, OPCEL[2]) > 5:
            #                 j = j + 1
            #         elif OPCOL[2] == 0:
            #             j = j + 1
            #         if OPCOL[3] != 0:
            #             if world.manhattan_distance(cel, OPCEL[3]) > 5:
            #                 j = j + 1
            #         elif OPCOL[3] == 0:
            #             j = j + 1
            #         if j == 4:
            #             good4.append(cel)
            #
            #         elif j == 3:
            #             good3.append(cel)
            #
            #         elif j == 2:
            #             good2.append(cel)
            #
            #         elif j == 1:
            #             good1.append(cel)
            #     if len(good4) != 0:
            #         ff = []
            #         B = []
            #         for gd in good4:
            #             if gd == CEL[0]:
            #                 bb = 1
            #                 break
            #             else:
            #                 ss = world.get_path_move_directions(start_cell=CEL[0], end_cell=gd)
            #                 if (len(ss) + FAZ - 1) < 7:
            #                     ff.append(gd)
            #         for fff in ff:
            #             dg = world.get_path_move_directions(start_cell=CEL[0], end_cell=fff)
            #             B.append(len(dg))
            #         if len(B) > 0:
            #             Y = B.index(min(B))
            #             if (B[Y] + FAZ - 1) < 7:
            #                 dg = world.get_path_move_directions(start_cell=CEL[0], end_cell=ff[Y])
            #                 if len(dg) > 0:
            #                     world.move_hero(hero=world.my_heroes[0], direction=dg[0])
            #                     uuu = 1
            #
            #     elif uuu == 0 and bb == 0 and len(good3) > 0:
            #         ff = []
            #         B = []
            #         for gd in good3:
            #             if gd == CEL[0]:
            #                 bb = 1
            #                 break
            #             else:
            #                 ss = world.get_path_move_directions(start_cell=CEL[0], end_cell=gd)
            #                 if (len(ss) + FAZ - 1) < 7:
            #                     ff.append(gd)
            #         for fff in ff:
            #             dg = world.get_path_move_directions(start_cell=CEL[0], end_cell=fff)
            #             B.append(len(dg))
            #         if len(B) > 0:
            #             Y = B.index(min(B))
            #             if (B[Y] + FAZ - 1) < 7:
            #                 dg = world.get_path_move_directions(start_cell=CEL[0], end_cell=ff[Y])
            #                 if len(dg) > 0:
            #                     world.move_hero(hero=world.my_heroes[0], direction=dg[0])
            #                     uuu = 1
            #
            #     elif uuu == 0 and bb == 0 and len(good2) > 0:
            #         ff = []
            #         B = []
            #         for gd in good2:
            #             if gd == CEL[0]:
            #                 bb = 1
            #                 break
            #             else:
            #                 ss = world.get_path_move_directions(start_cell=CEL[0], end_cell=gd)
            #                 if (len(ss) + FAZ - 1) < 7:
            #                     ff.append(gd)
            #         for fff in ff:
            #             dg = world.get_path_move_directions(start_cell=CEL[0], end_cell=fff)
            #             B.append(len(dg))
            #         if len(B) > 0:
            #             Y = B.index(min(B))
            #             if (B[Y] + FAZ - 1) < 7:
            #                 dg = world.get_path_move_directions(start_cell=CEL[0], end_cell=ff[Y])
            #                 if len(dg) > 0:
            #                     world.move_hero(hero=world.my_heroes[0], direction=dg[0])
            #                     uuu = 1
            #
            #     elif uuu == 0 and bb == 0 and len(good1) > 0:
            #         ff = []
            #         B = []
            #         for gd in good1:
            #             if gd == CEL[0]:
            #                 bb = 1
            #                 break
            #             else:
            #                 ss = world.get_path_move_directions(start_cell=CEL[0], end_cell=gd)
            #                 if (len(ss) + FAZ - 1) < 7:
            #                     ff.append(gd)
            #         for fff in ff:
            #             dg = world.get_path_move_directions(start_cell=CEL[0], end_cell=fff)
            #             B.append(len(dg))
            #         if len(B) > 0:
            #             Y = B.index(min(B))
            #             if (B[Y] + FAZ - 1) < 7:
            #                 dg = world.get_path_move_directions(start_cell=CEL[0], end_cell=ff[Y])
            #                 if len(dg) > 0:
            #                     world.move_hero(hero=world.my_heroes[0], direction=dg[0])
            #                     uuu = 1
            if uuu == 0 and bb == 0 and D == 0 and l ==0 and uuuu==0 and world.my_heroes[0].current_hp > 0 and l==0:
                if len(DO) > 0:
                    world.move_hero(hero=world.my_heroes[0], direction=DO[0])
                    uuu = 1
            D = 0
            bb = 0
            uuu = 0
            if h2 is True and uuu == 0 and l2 != 0 and D == 0 and FAZ>5 and world.my_heroes[2].current_hp > 0:
                i = 0
                j = 0
                good4 = []
                good1 = []
                good2 = []
                good3 = []
                uuu = 0
                bb = 0
                for cel in M:
                    j = 0
                    if OPCOL[0] != 0:
                        if world.manhattan_distance(cel, OPCEL[0]) < 3:
                            j = j + 1
                    if OPCOL[1] != 0:
                        if world.manhattan_distance(cel, OPCEL[1]) < 3:
                            j = j + 1
                    if OPCOL[2] != 0:
                        if world.manhattan_distance(cel, OPCEL[2]) < 3:
                            j = j + 1
                    if OPCOL[3] != 0:
                        if world.manhattan_distance(cel, OPCEL[3]) < 3:
                            j = j + 1
                    if j == 4:
                        good4.append(cel)

                    elif j == 3:
                        good3.append(cel)

                    elif j == 2:
                        good2.append(cel)

                    elif j == 1:
                        good1.append(cel)
                if len(good4) != 0:
                    ff = []
                    B = []
                    for gd in good4:
                        if world.manhattan_distance(CEL[2], gd) < 6:
                            bb = 1
                            break
                        else:
                            for cel in M:
                                if world.manhattan_distance(cel, gd) < 6:
                                    ff.append(cel)
                    if bb == 0 and uuu == 0:
                        for fff in ff:
                            dg = get_path_move_directions(start_cell=CEL[2], end_cell=fff, world=world)
                            B.append(len(dg))
                        if len(B) > 0:
                            Y = B.index(min(B))
                            if (B[Y] + FAZ - 1) < 7:
                                dg = get_path_move_directions(start_cell=CEL[2], end_cell=ff[Y], world=world)
                                if len(dg) > 0:
                                    world.move_hero(hero=world.my_heroes[2], direction=dg[0])
                                    uuu = 1

                elif uuu == 0 and bb == 0 and len(good3) > 0:
                    ff = []
                    B = []
                    for gd in good3:
                        if world.manhattan_distance(CEL[2], gd) < 6:
                            bb = 1
                            break
                        else:
                            for cel in M:
                                if world.manhattan_distance(cel, gd) < 6:
                                    ff.append(cel)
                    if bb == 0 and uuu == 0:
                        for fff in ff:
                            dg = get_path_move_directions(start_cell=CEL[2], end_cell=fff, world=world)
                            B.append(len(dg))
                        if len(B) > 0:
                            Y = B.index(min(B))
                            if (B[Y] + FAZ - 1) < 7:
                                dg = get_path_move_directions(start_cell=CEL[2], end_cell=ff[Y], world=world)
                                if len(dg) > 0:
                                    world.move_hero(hero=world.my_heroes[2], direction=dg[0])
                                    uuu = 1


                elif uuu == 0 and bb == 0 and len(good2) > 0:
                    fff2 = []
                    BB2 = []
                    for gd in good2:
                        if world.manhattan_distance(CEL[2], gd) < 6:
                            bb = 1
                            break
                        else:
                            for cel in M:
                                if world.manhattan_distance(cel, gd) < 6:
                                    fff2.append(cel)
                    if bb == 0 and uuu == 0:
                        for fff in fff2:
                            dg = get_path_move_directions(start_cell=CEL[2], end_cell=fff, world=world)
                            BB2.append(len(dg))
                        if len(BB2) > 0:
                            Y = BB2.index(min(BB2))
                            if (BB2[Y] + FAZ - 1) < 7:
                                dg = get_path_move_directions(start_cell=CEL[2], end_cell=fff2[Y], world=world)
                                if len(dg) > 0:
                                    world.move_hero(hero=world.my_heroes[2], direction=dg[0])
                                    uuu = 1
                elif uuu == 0 and bb == 0 and len(good1) > 0:
                    fff1 = []
                    BB1 = []
                    for gd in good1:
                        if world.manhattan_distance(CEL[2], gd) < 6:
                            bb = 1
                            break
                        else:
                            for cel in M:
                                if world.manhattan_distance(cel, gd) < 6:
                                    fff1.append(cel)
                    if bb == 0 and uuu == 0:
                        for fff in fff1:
                            dg = get_path_move_directions(start_cell=CEL[2], end_cell=fff, world=world)
                            BB1.append(len(dg))
                        if len(BB1) > 0:
                            Y = BB1.index(min(BB1))
                            if (BB1[Y] + FAZ - 1) < 7:
                                dg = get_path_move_directions(start_cell=CEL[2], end_cell=fff1[Y], world=world)
                                if len(dg) > 0:
                                    world.move_hero(hero=world.my_heroes[2], direction=dg[0])
                                    uuu = 1
            # if hhh2 is True and  bb == 0 and uuuu==0:
            #     uuuu = 0
            #     if OPCOL[0] != 0 and uuuu == 0:
            #         if world.opp_heroes[0].name == HeroName.BLASTER:
            #             ti = world.opp_heroes[0].get_ability(f).is_ready()
            #             if ti is True:
            #                 if world.manhattan_distance(CEL[2], OPCEL[0]) < 8:
            #                     for cel in M:
            #                         if world.manhattan_distance(start_cell=CEL[2], end_cell=cel) > 2 and cel != CEL[0] and cel != CEL[1] and cel != CEL[3] and uuuu == 0:
            #                             uuuu = 1
            #                             break
            #     if OPCOL[1] != 0 and uuuu == 0:
            #         if world.opp_heroes[1].name == HeroName.BLASTER:
            #             ti = world.opp_heroes[1].get_ability(f).is_ready()
            #             if ti is True:
            #                 if world.manhattan_distance(CEL[2], OPCEL[1]) < 8:
            #                     for cel in M:
            #                         if world.manhattan_distance(start_cell=CEL[2], end_cell=cel) > 2 and cel != CEL[0] and cel != CEL[1] and cel != CEL[3] and uuuu == 0:
            #                             uuuu = 1
            #                             break
            #     if OPCOL[2] != 0 and uuuu == 0:
            #         if world.opp_heroes[2].name == HeroName.BLASTER:
            #             ti = world.opp_heroes[2].get_ability(f).is_ready()
            #             if ti is True:
            #                 if world.manhattan_distance(CEL[2], OPCEL[2]) < 8:
            #                     for cel in M:
            #                         if world.manhattan_distance(start_cell=CEL[2], end_cell=cel) > 2 and cel != CEL[0] and cel != CEL[1] and cel != CEL[3] and uuuu == 0:
            #                             uuuu = 1
            #                             break
            #     if OPCOL[3] != 0 and uuuu == 0:
            #         if world.opp_heroes[3].name == HeroName.BLASTER:
            #             ti = world.opp_heroes[3].get_ability(f).is_ready()
            #             if ti is True:
            #                 if world.manhattan_distance(CEL[2], OPCEL[3]) < 8:
            #                     for cel in M:
            #                         if world.manhattan_distance(start_cell=CEL[2], end_cell=cel) > 2 and cel != CEL[0] and cel != CEL[1] and cel != CEL[3] and uuuu == 0:
            #                             uuuu = 1
            #                             break
            if hh2 is True and uuu == 0 and bb == 0 and l2 != 0 and D == 0 and h2 is False and FAZ>4 and hhh2 is False and uuuu==0 and world.my_heroes[2].current_hp > 0:
                Q = []
                for cel in M:
                    K = 0
                    if OPCOL[0] != 0:
                        if world.get_impact_cell(ability=world.my_heroes[2].get_ability(fa), start_cell=cel,target_cell=OPCEL[0]) == OPCEL[0]:
                            Q.append(cel)
                            K = 1
                    if OPCOL[1] != 0 and K == 0:
                        if world.get_impact_cell(ability=world.my_heroes[2].get_ability(fa), start_cell=cel,target_cell=OPCEL[1]) == OPCEL[1]:
                            Q.append(cel)
                            K = 1
                    if OPCOL[2] != 0 and K == 0:
                        if world.get_impact_cell(ability=world.my_heroes[2].get_ability(fa), start_cell=cel,target_cell=OPCEL[2]) == OPCEL[2]:
                            Q.append(cel)
                            K = 1
                    if OPCOL[3] != 0 and K == 0:
                        if world.get_impact_cell(ability=world.my_heroes[2].get_ability(fa), start_cell=cel,target_cell=OPCEL[3]) == OPCEL[3]:
                            Q.append(cel)
                            K = 1
                i = 0
                bbbb = []
                bbbb.clear()
                D = 0
                if len(Q) > 0:
                    for q in Q:
                        if q == CEL[2]:
                            D = 1
                            break
                        else:
                            e = get_path_move_directions(start_cell=CEL[2], end_cell=q, world=world)
                            s = len(e)
                            bbbb.append(s)
                    if len(bbbb) > 0:
                        a = bbbb.index(min(bbbb))
                        if D == 0:
                            e = get_path_move_directions(start_cell=CEL[2], end_cell=Q[a], world=world)
                            if len(e) > 0 and (len(e) + FAZ - 1) < 7:
                                world.move_hero(hero=world.my_heroes[2], direction=e[0])
                                uuu = 1
            # if hhh2 is False and uuu == 0 and bb == 0 and l2 != 0 and D == 0 and h2 is False and hh2 is False:
            #     i = 0
            #     j = 0
            #     good4 = []
            #     good1 = []
            #     good2 = []
            #     good3 = []
            #     uuu = 0
            #     bb = 0
            #     for cel in M:
            #         j = 0
            #         if OPCOL[0] != 0:
            #             if world.manhattan_distance(cel, OPCEL[0]) > 5:
            #                 j = j + 1
            #         elif OPCOL[0] == 0:
            #             j = j + 1
            #         if OPCOL[1] != 0:
            #             if world.manhattan_distance(cel, OPCEL[1]) > 5:
            #                 j = j + 1
            #         elif OPCOL[1] == 0:
            #             j = j + 1
            #         if OPCOL[2] != 0:
            #             if world.manhattan_distance(cel, OPCEL[2]) > 5:
            #                 j = j + 1
            #         elif OPCOL[2] == 0:
            #             j = j + 1
            #         if OPCOL[3] != 0:
            #             if world.manhattan_distance(cel, OPCEL[3]) > 5:
            #                 j = j + 1
            #         elif OPCOL[3] == 0:
            #             j = j + 1
            #         if j == 4:
            #             good4.append(cel)
            #
            #         elif j == 3:
            #             good3.append(cel)
            #
            #         elif j == 2:
            #             good2.append(cel)
            #
            #         elif j == 1:
            #             good1.append(cel)
            #     if len(good4) != 0:
            #         ff = []
            #         B = []
            #         for gd in good4:
            #             if gd == CEL[2]:
            #                 bb = 1
            #                 break
            #             else:
            #                 ss = world.get_path_move_directions(start_cell=CEL[2], end_cell=gd)
            #                 if (len(ss) + FAZ - 1) < 7:
            #                     ff.append(gd)
            #         if bb == 0 and uuu == 0:
            #             for fff in ff:
            #                 dg = world.get_path_move_directions(start_cell=CEL[2], end_cell=fff)
            #                 B.append(len(dg))
            #             if len(B) > 0:
            #                 Y = B.index(min(B))
            #                 if (B[Y] + FAZ - 1) < 7:
            #                     dg = world.get_path_move_directions(start_cell=CEL[2], end_cell=ff[Y])
            #                     if len(dg) > 0:
            #                         world.move_hero(hero=world.my_heroes[2], direction=dg[0])
            #                         uuu = 1
            #     elif uuu == 0 and bb == 0 and len(good3) > 0:
            #         ff = []
            #         B = []
            #         for gd in good3:
            #             if gd == CEL[2]:
            #                 bb = 1
            #                 break
            #             else:
            #                 ss = world.get_path_move_directions(start_cell=CEL[2], end_cell=gd)
            #                 if (len(ss) + FAZ - 1) < 7:
            #                     ff.append(gd)
            #         if bb == 0 and uuu == 0:
            #             for fff in ff:
            #                 dg = world.get_path_move_directions(start_cell=CEL[2], end_cell=fff)
            #                 B.append(len(dg))
            #             if len(B) > 0:
            #                 Y = B.index(min(B))
            #                 if (B[Y] + FAZ - 1) < 7:
            #                     dg = world.get_path_move_directions(start_cell=CEL[2], end_cell=ff[Y])
            #                     if len(dg) > 0:
            #                         world.move_hero(hero=world.my_heroes[2], direction=dg[0])
            #                         uuu = 1
            #     elif uuu == 0 and bb == 0 and len(good2) > 0:
            #         ff = []
            #         B = []
            #         for gd in good2:
            #             if gd == CEL[2]:
            #                 bb = 1
            #                 break
            #             else:
            #                 ss = world.get_path_move_directions(start_cell=CEL[2], end_cell=gd)
            #                 if (len(ss) + FAZ - 1) < 7:
            #                     ff.append(gd)
            #         if bb == 0 and uuu == 0:
            #             for fff in ff:
            #                 dg = world.get_path_move_directions(start_cell=CEL[2], end_cell=fff)
            #                 B.append(len(dg))
            #             if len(B) > 0:
            #                 Y = B.index(min(B))
            #                 if (B[Y] + FAZ - 1) < 7:
            #                     dg = world.get_path_move_directions(start_cell=CEL[2], end_cell=ff[Y])
            #                     if len(dg) > 0:
            #                         world.move_hero(hero=world.my_heroes[2], direction=dg[0])
            #                         uuu = 1
            #     elif uuu == 0 and bb == 0 and len(good1) > 0:
            #         ff = []
            #         B = []
            #         for gd in good1:
            #             if gd == CEL[2]:
            #                 bb = 1
            #                 break
            #             else:
            #                 ss = world.get_path_move_directions(start_cell=CEL[2], end_cell=gd)
            #                 if (len(ss) + FAZ - 1) < 7:
            #                     ff.append(gd)
            #         if bb == 0 and uuu == 0:
            #             for fff in ff:
            #                 dg = world.get_path_move_directions(start_cell=CEL[2], end_cell=fff)
            #                 B.append(len(dg))
            #             if len(B) > 0:
            #                 Y = B.index(min(B))
            #                 if (B[Y] + FAZ - 1) < 7:
            #                     dg = world.get_path_move_directions(start_cell=CEL[2], end_cell=ff[Y])
            #                     if len(dg) > 0:
            #                         world.move_hero(hero=world.my_heroes[2], direction=dg[0])
            #                         uuu = 1
            if uuu == 0 and bb == 0 and D == 0 and l2 ==0 and uuuu==0 and world.my_heroes[2].current_hp > 0 and l2==0:
                if len(DO2) > 0:
                    world.move_hero(hero=world.my_heroes[2], direction=DO2[0])
                    uuu = 1
            bb = 0
            uuu = 0
            uuuu=0
            D = 0
            if h3 is True and uuu == 0 and l3 != 0 and D == 0 and FAZ>5 and world.my_heroes[3].current_hp > 0:
                i = 0
                j = 0
                good4 = []
                good1 = []
                good2 = []
                good3 = []
                uuu = 0
                bb = 0
                for cel in N:
                    j = 0
                    if OPCOL[0] != 0:
                        if world.manhattan_distance(cel, OPCEL[0]) < 3:
                            j = j + 1
                    if OPCOL[1] != 0:
                        if world.manhattan_distance(cel, OPCEL[1]) < 3:
                            j = j + 1
                    if OPCOL[2] != 0:
                        if world.manhattan_distance(cel, OPCEL[2]) < 3:
                            j = j + 1
                    if OPCOL[3] != 0:
                        if world.manhattan_distance(cel, OPCEL[3]) < 3:
                            j = j + 1
                    if j == 4:
                        good4.append(cel)

                    elif j == 3:
                        good3.append(cel)

                    elif j == 2:
                        good2.append(cel)

                    elif j == 1:
                        good1.append(cel)
                if len(good4) != 0:
                    ff = []
                    B = []
                    for gd in good4:
                        if world.manhattan_distance(CEL[3], gd) < 6:
                            bb = 1
                            break
                        else:
                            for cel in N:
                                if world.manhattan_distance(cel, gd) < 6:
                                    ff.append(cel)
                    if bb == 0 and uuu == 0:
                        for fff in ff:
                            dg = get_path_move_directions(start_cell=CEL[3], end_cell=fff, world=world)
                            B.append(len(dg))
                        if len(B) > 0:
                            Y = B.index(min(B))
                            if (B[Y] + FAZ - 1) < 7:
                                dg = get_path_move_directions(start_cell=CEL[3], end_cell=ff[Y], world=world)
                                if len(dg) > 0:
                                    world.move_hero(hero=world.my_heroes[3], direction=dg[0])
                                    uuu = 1

                elif uuu == 0 and bb == 0 and len(good3) > 0:
                    ff = []
                    B = []
                    for gd in good3:
                        if world.manhattan_distance(CEL[3], gd) < 6:
                            bb = 1
                            break
                        else:
                            for cel in N:
                                if world.manhattan_distance(cel, gd) < 6:
                                    ff.append(cel)
                    if bb == 0 and uuu == 0:
                        for fff in ff:
                            dg = get_path_move_directions(start_cell=CEL[3], end_cell=fff, world=world)
                            B.append(len(dg))
                        if len(B) > 0:
                            Y = B.index(min(B))
                            if (B[Y] + FAZ - 1) < 7:
                                dg = get_path_move_directions(start_cell=CEL[3], end_cell=ff[Y], world=world)
                                if len(dg) > 0:
                                    world.move_hero(hero=world.my_heroes[3], direction=dg[0])
                                    uuu = 1

                elif uuu == 0 and bb == 0 and len(good2) > 0:
                    fff2 = []
                    BB2 = []
                    for gd in good2:
                        if world.manhattan_distance(CEL[3], gd) < 6:
                            bb = 1
                            break
                        else:
                            for cel in N:
                                if world.manhattan_distance(cel, gd) < 6:
                                    fff2.append(cel)
                    if bb == 0 and uuu == 0:
                        for fff in fff2:
                            dg = get_path_move_directions(start_cell=CEL[3], end_cell=fff, world=world)
                            BB2.append(len(dg))
                        if len(BB2) > 0:
                            Y = BB2.index(min(BB2))
                            if (BB2[Y] + FAZ - 1) < 7:
                                dg = get_path_move_directions(start_cell=CEL[3], end_cell=fff2[Y], world=world)
                                if len(dg) > 0:
                                    world.move_hero(hero=world.my_heroes[3], direction=dg[0])
                                    uuu = 1

                elif uuu == 0 and bb == 0 and len(good1) > 0:
                    fffW = []
                    BBW = []
                    for gd in good1:
                        if world.manhattan_distance(CEL[3], gd) < 6:
                            bb = 1
                            break
                        else:
                            for cel in N:
                                if world.manhattan_distance(cel, gd) < 6:
                                    fffW.append(cel)
                    if bb == 0 and uuu == 0:
                        for fffff in fffW:
                            dg = get_path_move_directions(start_cell=CEL[3], end_cell=fffff, world=world)
                            BBW.append(len(dg))
                        if len(BBW) > 0:
                            Y = BBW.index(min(BBW))
                            if (BBW[Y] + FAZ - 1) < 7:
                                dg = get_path_move_directions(start_cell=CEL[3], end_cell=fffW[Y], world=world)
                                if len(dg) > 0:
                                    world.move_hero(hero=world.my_heroes[3], direction=dg[0])
                                    uuu = 1
            # if hhh3 is True and bb == 0 and uuuu==0:
            #     uuuu = 0
            #     if OPCOL[0] != 0 and uuuu == 0:
            #         if world.opp_heroes[0].name == HeroName.BLASTER:
            #             ti = world.opp_heroes[0].get_ability(f).is_ready()
            #             if ti is True:
            #                 if world.manhattan_distance(CEL[3], OPCEL[0]) < 8:
            #                     for cel in N:
            #                         if world.manhattan_distance(start_cell=CEL[3], end_cell=cel) > 2 and cel != CEL[0] and cel != CEL[1] and cel != CEL[2] and uuuu == 0:
            #                             uuuu = 1
            #                             break
            #     if OPCOL[1] != 0 and uuuu == 0:
            #         if world.opp_heroes[1].name == HeroName.BLASTER:
            #             ti = world.opp_heroes[1].get_ability(f).is_ready()
            #             if ti is True:
            #                 if world.manhattan_distance(CEL[3], OPCEL[1]) < 8:
            #                     for cel in N:
            #                         if world.manhattan_distance(start_cell=CEL[3], end_cell=cel) > 2 and cel != CEL[0] and cel != CEL[1] and cel != CEL[2] and uuuu == 0:
            #                             uuuu = 1
            #                             break
            #     if OPCOL[2] != 0 and uuuu == 0:
            #         if world.opp_heroes[2].name == HeroName.BLASTER:
            #             ti = world.opp_heroes[2].get_ability(f).is_ready()
            #             if ti is True:
            #                 if world.manhattan_distance(CEL[3], OPCEL[2]) < 8:
            #                     for cel in N:
            #                         if world.manhattan_distance(start_cell=CEL[3], end_cell=cel) > 2 and cel != CEL[0] and cel != CEL[1] and cel != CEL[2] and uuuu == 0:
            #                             uuuu = 1
            #                             break
            #     if OPCOL[3] != 0 and uuuu == 0:
            #         if world.opp_heroes[3].name == HeroName.BLASTER:
            #             ti = world.opp_heroes[3].get_ability(f).is_ready()
            #             if ti is True:
            #                 if world.manhattan_distance(CEL[3], OPCEL[3]) < 8:
            #                     for cel in N:
            #                         if world.manhattan_distance(start_cell=CEL[3], end_cell=cel) > 2 and cel != CEL[0] and cel != CEL[1] and cel != CEL[2] and uuuu == 0:
            #                             uuuu = 1
            #                             break
            if hh3 is True and uuu == 0 and bb == 0 and l3 != 0 and D == 0 and h3 is False and FAZ>4 and hhh3 is False and  uuuu==0 and world.my_heroes[3].current_hp > 0:
                Q = []
                for cel in N:
                    K = 0
                    if OPCOL[0] != 0:
                        if world.get_impact_cell(ability=world.my_heroes[3].get_ability(fa), start_cell=cel,target_cell=OPCEL[0]) == OPCEL[0]:
                            Q.append(cel)
                            K = 1
                    if OPCOL[1] != 0 and K == 0:
                        if world.get_impact_cell(ability=world.my_heroes[3].get_ability(fa), start_cell=cel,target_cell=OPCEL[1]) == OPCEL[1]:
                            Q.append(cel)
                            K = 1
                    if OPCOL[2] != 0 and K == 0:
                        if world.get_impact_cell(ability=world.my_heroes[3].get_ability(fa), start_cell=cel,target_cell=OPCEL[2]) == OPCEL[2]:
                            Q.append(cel)
                            K = 1
                    if OPCOL[3] != 0 and K == 0:
                        if world.get_impact_cell(ability=world.my_heroes[3].get_ability(fa), start_cell=cel,target_cell=OPCEL[3]) == OPCEL[3]:
                            Q.append(cel)
                            K = 1
                i = 0
                bbbb = []
                bbbb.clear()
                D = 0
                if len(Q) > 0:
                    for q in Q:
                        if q == CEL[3]:
                            D = 1
                            break
                        else:
                            e = get_path_move_directions(start_cell=CEL[3], end_cell=q, world=world)
                            s = len(e)
                            bbbb.append(s)
                    if len(bbbb) > 0:
                        a = bbbb.index(min(bbbb))
                        if D == 0:
                            e = get_path_move_directions(start_cell=CEL[3], end_cell=Q[a], world=world)
                            if len(e) > 0 and (len(e) + FAZ - 1) < 7:
                                world.move_hero(hero=world.my_heroes[3], direction=e[0])
                                uuu = 1
            # if hhh3 is False and uuu == 0 and bb == 0 and l3 != 0 and D == 0 and h3 is False and hh3 is False:
            #     i = 0
            #     j = 0
            #     good4 = []
            #     good1 = []
            #     good2 = []
            #     good3 = []
            #     uuu = 0
            #     bb = 0
            #     for cel in N:
            #         j = 0
            #         if OPCOL[0] != 0:
            #             if world.manhattan_distance(cel, OPCEL[0]) > 5:
            #                 j = j + 1
            #         elif OPCOL[0] == 0:
            #             j = j + 1
            #         if OPCOL[1] != 0:
            #             if world.manhattan_distance(cel, OPCEL[1]) > 5:
            #                 j = j + 1
            #         elif OPCOL[1] == 0:
            #             j = j + 1
            #         if OPCOL[2] != 0:
            #             if world.manhattan_distance(cel, OPCEL[2]) > 5:
            #                 j = j + 1
            #         elif OPCOL[2] == 0:
            #             j = j + 1
            #         if OPCOL[3] != 0:
            #             if world.manhattan_distance(cel, OPCEL[3]) > 5:
            #                 j = j + 1
            #         elif OPCOL[3] == 0:
            #             j = j + 1
            #         if j == 4:
            #             good4.append(cel)
            #
            #         elif j == 3:
            #             good3.append(cel)
            #
            #         elif j == 2:
            #             good2.append(cel)
            #
            #         elif j == 1:
            #             good1.append(cel)
            #     if len(good4) != 0:
            #         ff = []
            #         B = []
            #         for gd in good4:
            #             if gd == CEL[3]:
            #                 bb = 1
            #                 break
            #             else:
            #                 ss = world.get_path_move_directions(start_cell=CEL[3], end_cell=gd)
            #                 if (len(ss) + FAZ - 1) < 7:
            #                     ff.append(gd)
            #         if bb == 0 and uuu == 0:
            #             for fff in ff:
            #                 dg = world.get_path_move_directions(start_cell=CEL[3], end_cell=fff)
            #                 B.append(len(dg))
            #             if len(B) > 0:
            #                 Y = B.index(min(B))
            #                 if (B[Y] + FAZ - 1) < 7:
            #                     dg = world.get_path_move_directions(start_cell=CEL[3], end_cell=ff[Y])
            #                     if len(dg) > 0:
            #                         world.move_hero(hero=world.my_heroes[3], direction=dg[0])
            #                         uuu = 1
            #
            #     elif uuu == 0 and bb == 0 and len(good3) > 0:
            #         ff = []
            #         B = []
            #         for gd in good3:
            #             if gd == CEL[3]:
            #                 bb = 1
            #                 break
            #             else:
            #                 ss = world.get_path_move_directions(start_cell=CEL[3], end_cell=gd)
            #                 if (len(ss) + FAZ - 1) < 7:
            #                     ff.append(gd)
            #         if bb == 0 and uuu == 0:
            #             for fff in ff:
            #                 dg = world.get_path_move_directions(start_cell=CEL[3], end_cell=fff)
            #                 B.append(len(dg))
            #             if len(B) > 0:
            #                 Y = B.index(min(B))
            #                 if (B[Y] + FAZ - 1) < 7:
            #                     dg = world.get_path_move_directions(start_cell=CEL[3], end_cell=ff[Y])
            #                     if len(dg) > 0:
            #                         world.move_hero(hero=world.my_heroes[3], direction=dg[0])
            #                         uuu = 1
            #
            #     elif uuu == 0 and bb == 0 and len(good2) > 0:
            #         ff = []
            #         B = []
            #         for gd in good2:
            #             if gd == CEL[3]:
            #                 bb = 1
            #                 break
            #             else:
            #                 ss = world.get_path_move_directions(start_cell=CEL[3], end_cell=gd)
            #                 if (len(ss) + FAZ - 1) < 7:
            #                     ff.append(gd)
            #         if bb == 0 and uuu == 0:
            #             for fff in ff:
            #                 dg = world.get_path_move_directions(start_cell=CEL[3], end_cell=fff)
            #                 B.append(len(dg))
            #             if len(B) > 0:
            #                 Y = B.index(min(B))
            #                 if (B[Y] + FAZ - 1) < 7:
            #                     dg = world.get_path_move_directions(start_cell=CEL[3], end_cell=ff[Y])
            #                     if len(dg) > 0:
            #                         world.move_hero(hero=world.my_heroes[3], direction=dg[0])
            #                         uuu = 1
            #
            #     elif uuu == 0 and bb == 0 and len(good1) > 0:
            #         ff = []
            #         B = []
            #         for gd in good1:
            #             if gd == CEL[3]:
            #                 bb = 1
            #                 break
            #             else:
            #                 ss = world.get_path_move_directions(start_cell=CEL[3], end_cell=gd)
            #                 if (len(ss) + FAZ - 1) < 7:
            #                     ff.append(gd)
            #         if bb == 0 and uuu == 0:
            #             for fff in ff:
            #                 dg = world.get_path_move_directions(start_cell=CEL[3], end_cell=fff)
            #                 B.append(len(dg))
            #             if len(B) > 0:
            #                 Y = B.index(min(B))
            #                 if (B[Y] + FAZ - 1) < 7:
            #                     dg = world.get_path_move_directions(start_cell=CEL[3], end_cell=ff[Y])
            #                     if len(dg) > 0:
            #                         world.move_hero(hero=world.my_heroes[3], direction=dg[0])
            #                         uuu = 1
            if uuu == 0 and bb == 0 and D == 0 and l3 ==0 and uuuu==0 and world.my_heroes[3].current_hp > 0 and l3==0:
                if len(DO3) > 0:
                    world.move_hero(hero=world.my_heroes[3], direction=DO3[0])
                    uuu = 1

    def action(self, world):
        print("action")
        c = world.map.objective_zone
        r = world.map.opp_respawn_zone
        co = []
        ro = []
        D=0
        OPCEL = [0, 0, 0, 0]
        OPROW = [0, 0, 0, 0]
        OPCOL = [0, 0, 0, 0]
        OPHP = [0, 0, 0, 0]
        rores = [0, 0, 0, 0]
        cores = [0, 0, 0, 0]
        i = 0
        for ophero in world.opp_heroes:
            opcel = ophero.current_cell
            row = opcel.row
            if row != -1:
                OPHP[i] = ophero.current_hp
            i = i + 1
        i = 0
        for ophero in world.opp_heroes:
            opcel = ophero.current_cell
            row = opcel.row
            if row != -1:
                OPCEL[i] = ophero.current_cell
                OPCOL[i] = OPCEL[i].column
                OPROW[i] = OPCEL[i].row
            i = i + 1
        HP = [0, 0, 0, 0]
        CEL = [0, 0, 0, 0]
        COL = [0, 0, 0, 0]
        ROW = [0, 0,0, 0]
        i = 0
        for hero in world.my_heroes:
            HP[i] = hero.current_hp
            i = i + 1
        i = 0
        for hero in world.my_heroes:
            CEL[i] = hero.current_cell
            COL[i] = CEL[i].column
            ROW[i] = CEL[i].row
            i = i + 1
        FAZ = world.move_phase_num
        U = len(c)
        A = U // 2
        V = U // 4
        VV = (U // 4) * 3
        E = []
        T = []
        for cel in c:
            ui = cel.row
            iu = cel.column
            E.append(ui)
            T.append(iu)
        mxro = max(E)
        mxco = max(T)
        miro = min(E)
        mico = min(T)
        R = c[0].row
        C = c[0].column
        G = []
        H = []
        M = []
        N = []
        for cel in c:
            r = cel.row
            cl = cel.column
            if r >= miro and r <= ((mxro + miro) // 2) and cl >= mico and cl <= ((mxco + mico) // 2):
                G.append(cel)
            elif r > (((mxro + miro) // 2)) and cl >= mico and cl <= ((mxco + mico) // 2):
                H.append(cel)
            elif r > (((mxro + miro) // 2)) and cl > ((mxco + mico) // 2):
                N.append(cel)
            elif r >= miro and r <= ((mxro + miro) // 2) and cl > ((mxco + mico) // 2):
                M.append(cel)
        b = []
        i = 0
        w = 1000
        f = AbilityName.BLASTER_BOMB
        h = world.my_heroes[0].get_ability(f).is_ready()
        h1 = world.my_heroes[1].get_ability(f).is_ready()
        h2 = world.my_heroes[2].get_ability(f).is_ready()
        h3 = world.my_heroes[3].get_ability(f).is_ready()
        fa = AbilityName.BLASTER_ATTACK
        hh = world.my_heroes[0].get_ability(fa).is_ready()
        hh1 = world.my_heroes[1].get_ability(fa).is_ready()
        hh2 = world.my_heroes[2].get_ability(fa).is_ready()
        hh3 = world.my_heroes[3].get_ability(fa).is_ready()
        faa = AbilityName.BLASTER_DODGE
        hhh = world.my_heroes[0].get_ability(faa).is_ready()
        hhh1 = world.my_heroes[1].get_ability(faa).is_ready()
        hhh2 = world.my_heroes[2].get_ability(faa).is_ready()
        hhh3 = world.my_heroes[3].get_ability(faa).is_ready()
        bb=0
        p=0
        if h1 is True :
            i = 0
            j = 0
            good4 = []
            good1 = []
            good2 = []
            good3 = []
            uuu = 0
            bb = 0
            for cel in c:
                j=0
                if OPCOL[0] != 0:
                    if world.manhattan_distance(cel, OPCEL[0]) < 3:
                        j = j + 1
                if OPCOL[1] != 0:
                    if world.manhattan_distance(cel, OPCEL[1]) < 3:
                        j = j + 1
                if OPCOL[2] != 0:
                    if world.manhattan_distance(cel, OPCEL[2]) < 3:
                        j = j + 1
                if OPCOL[3] != 0:
                    if world.manhattan_distance(cel, OPCEL[3]) < 3:
                        j = j + 1
                if j == 4:
                    good4.append(cel)
                elif j == 3:
                    good3.append(cel)
                elif j == 2:
                    good2.append(cel)
                elif j == 1:
                    good1.append(cel)
            if len(good4) > 0:
                bb=0
                for gd in good4:
                    if world.manhattan_distance(CEL[1], gd) < 6 and bb==0:
                        bb = 1
                        world.cast_ability(hero=world.my_heroes[1],ability=world.my_heroes[1].get_ability(f),cell=gd)
                        break
            elif bb == 0 and len(good3) > 0:
                for gd in good3:
                    if world.manhattan_distance(CEL[1], gd) < 6 and bb==0:
                        bb = 1
                        world.cast_ability(hero=world.my_heroes[1], ability=world.my_heroes[1].get_ability(f), cell=gd)
                        break
            elif  bb == 0 and len(good2) > 0:
                for gd in good2:
                    if world.manhattan_distance(CEL[1], gd) < 6 and bb==0:
                        world.cast_ability(hero=world.my_heroes[1], ability=world.my_heroes[1].get_ability(f), cell=gd)
                        bb = 1
                        break
            elif bb == 0 and len(good1) > 0:
                for gd in good1:
                    if world.manhattan_distance(CEL[1], gd) < 6 and bb==0:
                        world.cast_ability(hero=world.my_heroes[1], ability=world.my_heroes[1].get_ability(f), cell=gd)
                        bb = 1
                        break
        if hhh1 is True and p ==0 and bb ==0 and h1 is False :
            uuuu=0
            if OPCOL[0]!=0 :
                if world.manhattan_distance(CEL[1],OPCEL[0])<6:
                    for cel in H:
                            if world.manhattan_distance(start_cell=CEL[1],end_cell= cel) > 2 and cel != CEL[0] and cel != CEL[2] and cel != CEL[3] and uuuu == 0:
                                world.cast_ability(hero=world.my_heroes[1], ability=world.my_heroes[1].get_ability(faa),cell=cel)
                                uuuu = 1
                                break

            if OPCOL[1] !=0 and uuuu==0:
                if world.manhattan_distance(CEL[1],OPCEL[1])<6 :
                    for cel in H:
                            if world.manhattan_distance(CEL[1], cel) > 2 and cel != CEL[0] and cel != CEL[2] and cel != CEL[3] and uuuu == 0:
                                world.cast_ability(hero=world.my_heroes[1], ability=world.my_heroes[1].get_ability(faa),cell=cel)
                                uuuu = 1
                                break

            if OPCOL[2] !=0 and uuuu==0:
                if world.manhattan_distance(CEL[1],OPCEL[2])<6 :
                    for cel in H:
                            if world.manhattan_distance(CEL[1], cel) > 2 and cel != CEL[0] and cel != CEL[2] and cel != CEL[3] and uuuu == 0:
                                world.cast_ability(hero=world.my_heroes[1], ability=world.my_heroes[1].get_ability(faa),cell=cel)
                                uuuu = 1
                                break

            if OPCOL[3] !=0 and uuuu==0:
                if world.manhattan_distance(CEL[1],OPCEL[3])<6 :
                    for cel in H:
                            if world.manhattan_distance(CEL[1], cel) > 2 and cel != CEL[0] and cel != CEL[2] and cel != CEL[3] and uuuu == 0:
                                world.cast_ability(hero=world.my_heroes[1], ability=world.my_heroes[1].get_ability(faa),cell=cel)
                                uuuu = 1
                                break
        if hh1 is True and bb ==0 and h1 is False :
            p=0
            if OPCOL[2] != 0:
                    if world.get_impact_cell(ability=world.my_heroes[1].get_ability(fa), start_cell=CEL[1], target_cell=OPCEL[2]) == OPCEL[2]:
                        world.cast_ability(hero=world.my_heroes[1],ability=world.my_heroes[1].get_ability(fa),cell=OPCEL[2])
                        P=1
            if OPCOL[0] != 0 and p==0 :
                    if world.get_impact_cell(ability=world.my_heroes[1].get_ability(fa), start_cell=CEL[1], target_cell=OPCEL[0]) == OPCEL[0]:
                        world.cast_ability(hero=world.my_heroes[1],ability=world.my_heroes[1].get_ability(fa),cell=OPCEL[0])
                        P = 1
            if OPCOL[1] != 0 and p==0:
                    if world.get_impact_cell(ability=world.my_heroes[1].get_ability(fa), start_cell=CEL[1], target_cell=OPCEL[1]) == OPCEL[1]:
                        world.cast_ability(hero=world.my_heroes[1],ability=world.my_heroes[1].get_ability(fa),cell=OPCEL[1])
                        P = 1
            if OPCOL[3] != 0 and p==0:
                    if world.get_impact_cell(ability=world.my_heroes[1].get_ability(fa), start_cell=CEL[1], target_cell=OPCEL[3]) == OPCEL[3]:
                        world.cast_ability(hero=world.my_heroes[1],ability=world.my_heroes[1].get_ability(fa),cell=OPCEL[3])
                        P = 1
        p = 0
        bb=0
        if h is True :
            i = 0
            j = 0
            good4 = []
            good1 = []
            good2 = []
            good3 = []
            uuu = 0
            bb = 0
            for cel in c:
                j=0
                if OPCOL[0] != 0:
                    if world.manhattan_distance(cel, OPCEL[0]) < 3:
                        j = j + 1
                if OPCOL[1] != 0:
                    if world.manhattan_distance(cel, OPCEL[1]) < 3:
                        j = j + 1
                if OPCOL[2] != 0:
                    if world.manhattan_distance(cel, OPCEL[2]) < 3:
                        j = j + 1
                if OPCOL[3] != 0:
                    if world.manhattan_distance(cel, OPCEL[3]) < 3:
                        j = j + 1
                if j == 4:
                    good4.append(cel)
                elif j == 3:
                    good3.append(cel)
                elif j == 2:
                    good2.append(cel)
                elif j == 1:
                    good1.append(cel)
            if len(good4) > 0:
                bb=0
                for gd in good4:
                    if world.manhattan_distance(CEL[0], gd) < 6 and bb==0:
                        bb = 1
                        world.cast_ability(hero=world.my_heroes[0],ability=world.my_heroes[0].get_ability(f),cell=gd)
                        break
            elif bb == 0 and len(good3) > 0:
                for gd in good3:
                    if world.manhattan_distance(CEL[0], gd) < 6 and bb==0:
                        bb = 1
                        world.cast_ability(hero=world.my_heroes[0], ability=world.my_heroes[0].get_ability(f), cell=gd)
                        break
            elif  bb == 0 and len(good2) > 0:
                for gd in good2:
                    if world.manhattan_distance(CEL[0], gd) < 6 and bb==0:
                        world.cast_ability(hero=world.my_heroes[0], ability=world.my_heroes[0].get_ability(f), cell=gd)
                        bb = 1
                        break
            elif bb == 0 and len(good1) > 0:
                for gd in good1:
                    if world.manhattan_distance(CEL[0], gd) < 6 and bb==0:
                        world.cast_ability(hero=world.my_heroes[0], ability=world.my_heroes[0].get_ability(f), cell=gd)
                        bb = 1
                        break
        if hhh is True and p ==0 and bb ==0 and h is False :
            uuuu=0
            if OPCOL[0]!=0 :
                if world.manhattan_distance(CEL[0],OPCEL[0])<6:
                    for cel in G:
                            if world.manhattan_distance(CEL[0], cel) > 2 and cel != CEL[1] and cel != CEL[2] and cel != CEL[3] and uuuu == 0:
                                world.cast_ability(hero=world.my_heroes[0], ability=world.my_heroes[0].get_ability(faa),cell=cel)
                                uuuu = 1
                                break

            if OPCOL[1] !=0 and uuuu==0:
                if world.manhattan_distance(CEL[0],OPCEL[1])<6 :
                    for cel in G:
                            if world.manhattan_distance(CEL[0], cel) > 2 and cel != CEL[1] and cel != CEL[2] and cel != CEL[3] and uuuu == 0:
                                world.cast_ability(hero=world.my_heroes[0], ability=world.my_heroes[0].get_ability(faa),cell=cel)
                                uuuu = 1
                                break

            if OPCOL[2] !=0 and uuuu==0:
                if world.manhattan_distance(CEL[0],OPCEL[2])<6 :
                    for cel in G:
                            if world.manhattan_distance(CEL[0], cel) > 2 and cel != CEL[1] and cel != CEL[2] and cel != CEL[3] and uuuu == 0:
                                world.cast_ability(hero=world.my_heroes[0], ability=world.my_heroes[0].get_ability(faa),cell=cel)
                                uuuu = 1
                                break

            if OPCOL[3] !=0 and uuuu==0:
                if world.manhattan_distance(CEL[0],OPCEL[3])<6 :
                    for cel in G:
                            if world.manhattan_distance(CEL[0], cel) > 2 and cel != CEL[1] and cel != CEL[2] and cel != CEL[3] and uuuu == 0:
                                world.cast_ability(hero=world.my_heroes[0], ability=world.my_heroes[0].get_ability(faa),cell=cel)
                                uuuu = 1
                                break
        if hh is True and bb ==0 :
            p=0
            if OPCOL[2] != 0:
                    if world.get_impact_cell(ability=world.my_heroes[0].get_ability(fa), start_cell=CEL[0], target_cell=OPCEL[2]) == OPCEL[2]:
                        world.cast_ability(hero=world.my_heroes[0],ability=world.my_heroes[0].get_ability(fa),cell=OPCEL[2])
                        P=1
            if OPCOL[0] != 0 and p==0 :
                    if world.get_impact_cell(ability=world.my_heroes[0].get_ability(fa), start_cell=CEL[0], target_cell=OPCEL[0]) == OPCEL[0]:
                        world.cast_ability(hero=world.my_heroes[0],ability=world.my_heroes[0].get_ability(fa),cell=OPCEL[0])
                        P = 1
            if OPCOL[1] != 0 and p==0:
                    if world.get_impact_cell(ability=world.my_heroes[0].get_ability(fa), start_cell=CEL[0], target_cell=OPCEL[1]) == OPCEL[1]:
                        world.cast_ability(hero=world.my_heroes[0],ability=world.my_heroes[0].get_ability(fa),cell=OPCEL[1])
                        P = 1
            if OPCOL[3] != 0 and p==0:
                    if world.get_impact_cell(ability=world.my_heroes[0].get_ability(fa), start_cell=CEL[0], target_cell=OPCEL[3]) == OPCEL[3]:
                        world.cast_ability(hero=world.my_heroes[0],ability=world.my_heroes[0].get_ability(fa),cell=OPCEL[3])
                        P = 1
        p = 0
        bb=0
        if h2 is True :
            i = 0
            j = 0
            good4 = []
            good1 = []
            good2 = []
            good3 = []
            uuu = 0
            bb = 0
            for cel in c:
                j = 0
                if OPCOL[0] != 0:
                    if world.manhattan_distance(cel, OPCEL[0]) < 3:
                        j = j + 1
                if OPCOL[1] != 0:
                    if world.manhattan_distance(cel, OPCEL[1]) < 3:
                        j = j + 1
                if OPCOL[2] != 0:
                    if world.manhattan_distance(cel, OPCEL[2]) < 3:
                        j = j + 1
                if OPCOL[3] != 0:
                    if world.manhattan_distance(cel, OPCEL[3]) < 3:
                        j = j + 1
                if j == 4:
                    good4.append(cel)
                elif j == 3:
                    good3.append(cel)
                elif j == 2:
                    good2.append(cel)
                elif j == 1:
                    good1.append(cel)
            if len(good4) > 0:
                bb = 0
                for gd in good4:
                    if world.manhattan_distance(CEL[2], gd) < 6 and bb == 0:
                        bb = 1
                        world.cast_ability(hero=world.my_heroes[2], ability=world.my_heroes[2].get_ability(f), cell=gd)
                        break
            elif bb == 0 and len(good3) > 0:
                for gd in good3:
                    if world.manhattan_distance(CEL[2], gd) < 6 and bb == 0:
                        bb = 1
                        world.cast_ability(hero=world.my_heroes[2], ability=world.my_heroes[2].get_ability(f), cell=gd)
                        break
            elif bb == 0 and len(good2) > 0:
                for gd in good2:
                    if world.manhattan_distance(CEL[2], gd) < 6 and bb == 0:
                        world.cast_ability(hero=world.my_heroes[2], ability=world.my_heroes[2].get_ability(f), cell=gd)
                        bb = 1
                        break
            elif bb == 0 and len(good1) > 0:
                for gd in good1:
                    if world.manhattan_distance(CEL[2], gd) < 6 and bb == 0:
                        world.cast_ability(hero=world.my_heroes[2], ability=world.my_heroes[2].get_ability(f), cell=gd)
                        bb = 1
                        break
        if hhh2 is True and p == 0 and bb == 0 and h2 is False:
            uuuu=0
            if OPCOL[0]!=0 :
                if world.manhattan_distance(CEL[2],OPCEL[0])<6:
                    for cel in M:
                            if world.manhattan_distance(CEL[2], cel) > 2 and cel != CEL[1] and cel != CEL[0] and cel != CEL[3] and uuuu == 0:
                                world.cast_ability(hero=world.my_heroes[2], ability=world.my_heroes[2].get_ability(faa),cell=cel)
                                uuuu = 1
                                break

            if OPCOL[1] !=0 and uuuu==0:
                if world.manhattan_distance(CEL[2],OPCEL[1])<6 :
                    for cel in M:
                            if world.manhattan_distance(CEL[2], cel) > 2 and cel != CEL[1] and cel != CEL[0] and cel != CEL[3] and uuuu == 0:
                                world.cast_ability(hero=world.my_heroes[2], ability=world.my_heroes[2].get_ability(faa),cell=cel)
                                uuuu = 1
                                break

            if OPCOL[2] !=0 and uuuu==0:
                if world.manhattan_distance(CEL[2],OPCEL[2])<6 :
                    for cel in M:
                            if world.manhattan_distance(CEL[2], cel) > 2 and cel != CEL[1] and cel != CEL[0] and cel != CEL[3] and uuuu == 0:
                                world.cast_ability(hero=world.my_heroes[2], ability=world.my_heroes[2].get_ability(faa),cell=cel)
                                uuuu = 1
                                break

            if OPCOL[3] !=0 and uuuu==0:
                if world.manhattan_distance(CEL[2],OPCEL[3])<6 :
                    for cel in M:
                            if world.manhattan_distance(CEL[2], cel) > 2 and cel != CEL[1] and cel != CEL[0] and cel != CEL[3] and uuuu == 0:
                                world.cast_ability(hero=world.my_heroes[2], ability=world.my_heroes[2].get_ability(faa),cell=cel)
                                uuuu = 1
                                break
        if hh2 is True and bb ==0  :
            p=0
            if OPCOL[2] != 0:
                    if world.get_impact_cell(ability=world.my_heroes[2].get_ability(fa), start_cell=CEL[2], target_cell=OPCEL[2]) == OPCEL[2]:
                        world.cast_ability(hero=world.my_heroes[2],ability=world.my_heroes[2].get_ability(fa),cell=OPCEL[2])
                        P=1
            if OPCOL[0] != 0 and p==0 :
                    if world.get_impact_cell(ability=world.my_heroes[2].get_ability(fa), start_cell=CEL[2], target_cell=OPCEL[0]) == OPCEL[0]:
                        world.cast_ability(hero=world.my_heroes[2],ability=world.my_heroes[2].get_ability(fa),cell=OPCEL[0])
                        P = 1
            if OPCOL[1] != 0 and p==0:
                    if world.get_impact_cell(ability=world.my_heroes[2].get_ability(fa), start_cell=CEL[2], target_cell=OPCEL[1]) == OPCEL[1]:
                        world.cast_ability(hero=world.my_heroes[2],ability=world.my_heroes[2].get_ability(fa),cell=OPCEL[1])
                        P = 1
            if OPCOL[3] != 0 and p==0:
                    if world.get_impact_cell(ability=world.my_heroes[2].get_ability(fa), start_cell=CEL[2], target_cell=OPCEL[3]) == OPCEL[3]:
                        world.cast_ability(hero=world.my_heroes[2],ability=world.my_heroes[2].get_ability(fa),cell=OPCEL[3])
                        P = 1
        p = 0
        bb = 0
        if h3 is True :
            i = 0
            j = 0
            good4 = []
            good1 = []
            good2 = []
            good3 = []
            uuu = 0
            bb = 0
            for cel in c:
                j = 0
                if OPCOL[0] != 0:
                    if world.manhattan_distance(cel, OPCEL[0]) < 3:
                        j = j + 1
                if OPCOL[1] != 0:
                    if world.manhattan_distance(cel, OPCEL[1]) < 3:
                        j = j + 1
                if OPCOL[2] != 0:
                    if world.manhattan_distance(cel, OPCEL[2]) < 3:
                        j = j + 1
                if OPCOL[3] != 0:
                    if world.manhattan_distance(cel, OPCEL[3]) < 3:
                        j = j + 1
                if j == 4:
                    good4.append(cel)
                elif j == 3:
                    good3.append(cel)
                elif j == 2:
                    good2.append(cel)
                elif j == 1:
                    good1.append(cel)
            if len(good4) > 0:
                bb = 0
                for gd in good4:
                    if world.manhattan_distance(CEL[3], gd) < 6 and bb == 0:
                        bb = 1
                        world.cast_ability(hero=world.my_heroes[3], ability=world.my_heroes[3].get_ability(f), cell=gd)
                        break
            elif bb == 0 and len(good3) > 0:
                for gd in good3:
                    if world.manhattan_distance(CEL[3], gd) < 6 and bb == 0:
                        bb = 1
                        world.cast_ability(hero=world.my_heroes[3], ability=world.my_heroes[3].get_ability(f), cell=gd)
                        break
            elif bb == 0 and len(good2) > 0:
                for gd in good2:
                    if world.manhattan_distance(CEL[3], gd) < 6 and bb == 0:
                        world.cast_ability(hero=world.my_heroes[3], ability=world.my_heroes[3].get_ability(f), cell=gd)
                        bb = 1
                        break
            elif bb == 0 and len(good1) > 0:
                for gd in good1:
                    if world.manhattan_distance(CEL[3], gd) < 6 and bb == 0:
                        world.cast_ability(hero=world.my_heroes[3], ability=world.my_heroes[3].get_ability(f), cell=gd)
                        bb = 1
                        break
        if hhh3 is True and p ==0 and bb ==0 and h3 is False:
            uuuu=0
            if OPCOL[0]!=0 :
                if world.manhattan_distance(CEL[3],OPCEL[0])<6:
                    for cel in N:
                            if world.manhattan_distance(CEL[3], cel) > 2 and cel != CEL[1] and cel != CEL[2] and cel != CEL[0] and uuuu == 0:
                                world.cast_ability(hero=world.my_heroes[3], ability=world.my_heroes[3].get_ability(faa),cell=cel)
                                uuuu = 1
                                break

            if OPCOL[1] !=0 and uuuu==0:
                if world.manhattan_distance(CEL[3],OPCEL[1])<6 :
                    for cel in N:
                            if world.manhattan_distance(CEL[3], cel) > 2 and cel != CEL[1] and cel != CEL[2] and cel != CEL[0] and uuuu == 0:
                                world.cast_ability(hero=world.my_heroes[3], ability=world.my_heroes[3].get_ability(faa),cell=cel)
                                uuuu = 1
                                break

            if OPCOL[2] !=0 and uuuu==0:
                if world.manhattan_distance(CEL[3],OPCEL[2])<6 :
                     for cel in N:
                            if world.manhattan_distance(CEL[3], cel) > 2 and cel != CEL[1] and cel != CEL[2] and cel != CEL[0] and uuuu == 0:
                                world.cast_ability(hero=world.my_heroes[3], ability=world.my_heroes[3].get_ability(faa),cell=cel)
                                uuuu = 1
                                break

            if OPCOL[3] !=0 and uuuu==0:
                if world.manhattan_distance(CEL[3],OPCEL[3])<6 :
                    for cel in N:
                            if world.manhattan_distance(CEL[3], cel) > 2 and cel != CEL[1] and cel != CEL[2] and cel != CEL[0] and uuuu == 0:
                                world.cast_ability(hero=world.my_heroes[3], ability=world.my_heroes[3].get_ability(faa),cell=cel)
                                uuuu = 1
                                break
            # uuuu=0
            # if OPCOL[0] != 0 and uuuu==0:
            #     if world.opp_heroes[0].name == HeroName.BLASTER:
            #         ti = world.opp_heroes[0].get_ability(f).is_ready()
            #         if ti is True:
            #             if world.manhattan_distance(CEL[3], OPCEL[0]) < 8:
            #                 for cel in N:
            #                     if world.manhattan_distance(start_cell=CEL[3], end_cell=cel) > 2 and cel != CEL[0] and cel != CEL[1] and cel != CEL[2] and uuuu == 0:
            #                         world.cast_ability(hero=world.my_heroes[3],ability=world.my_heroes[3].get_ability(faa), cell=cel)
            #                         uuuu = 1
            #                         break
            # if OPCOL[1] != 0 and uuuu==0:
            #     if world.opp_heroes[1].name == HeroName.BLASTER:
            #         ti = world.opp_heroes[1].get_ability(f).is_ready()
            #         if ti is True:
            #             if world.manhattan_distance(CEL[3], OPCEL[1]) < 8:
            #                 for cel in N:
            #                     if world.manhattan_distance(start_cell=CEL[3], end_cell=cel) > 2 and cel != CEL[0] and cel != CEL[1] and cel != CEL[2] and uuuu == 0:
            #                         world.cast_ability(hero=world.my_heroes[3],ability=world.my_heroes[3].get_ability(faa), cell=cel)
            #                         uuuu = 1
            #                         break
            # if OPCOL[2] != 0 and uuuu==0:
            #     if world.opp_heroes[2].name == HeroName.BLASTER:
            #         ti = world.opp_heroes[2].get_ability(f).is_ready()
            #         if ti is True:
            #             if world.manhattan_distance(CEL[3], OPCEL[2]) < 8:
            #                 for cel in N:
            #                     if world.manhattan_distance(start_cell=CEL[3], end_cell=cel) > 2 and cel != CEL[0] and cel != CEL[1] and cel != CEL[2] and uuuu == 0:
            #                         world.cast_ability(hero=world.my_heroes[3],ability=world.my_heroes[3].get_ability(faa), cell=cel)
            #                         uuuu = 1
            #                         break
            if OPCOL[3] != 0 and uuuu==0:
                if world.opp_heroes[3].name == HeroName.BLASTER:
                    ti = world.opp_heroes[3].get_ability(f).is_ready()
                    if ti is True:
                        if world.manhattan_distance(CEL[3], OPCEL[3]) < 8:
                            for cel in N:
                                if world.manhattan_distance(start_cell=CEL[3], end_cell=cel) > 2 and cel != CEL[0] and cel != CEL[1] and cel != CEL[2] and uuuu == 0:
                                    world.cast_ability(hero=world.my_heroes[3],ability=world.my_heroes[3].get_ability(faa), cell=cel)
                                    uuuu = 1
                                    break
        if hh3 is True and bb ==0 :
            p=0
            if OPCOL[2] != 0:
                    if world.get_impact_cell(ability=world.my_heroes[3].get_ability(fa), start_cell=CEL[3], target_cell=OPCEL[2]) == OPCEL[2]:
                        world.cast_ability(hero=world.my_heroes[3],ability=world.my_heroes[3].get_ability(fa),cell=OPCEL[2])
                        P=1
            if OPCOL[0] != 0 and p==0 :
                    if world.get_impact_cell(ability=world.my_heroes[3].get_ability(fa), start_cell=CEL[3], target_cell=OPCEL[0]) == OPCEL[0]:
                        world.cast_ability(hero=world.my_heroes[3],ability=world.my_heroes[3].get_ability(fa),cell=OPCEL[0])
                        P = 1
            if OPCOL[1] != 0 and p==0:
                    if world.get_impact_cell(ability=world.my_heroes[3].get_ability(fa), start_cell=CEL[3], target_cell=OPCEL[1]) == OPCEL[1]:
                        world.cast_ability(hero=world.my_heroes[3],ability=world.my_heroes[3].get_ability(fa),cell=OPCEL[1])
                        P = 1
            if OPCOL[3] != 0 and p==0:
                    if world.get_impact_cell(ability=world.my_heroes[3].get_ability(fa), start_cell=CEL[3], target_cell=OPCEL[3]) == OPCEL[3]:
                        world.cast_ability(hero=world.my_heroes[3],ability=world.my_heroes[3].get_ability(fa),cell=OPCEL[3])
                        P = 1

        # mnn=world.my_score
        # onn=world.opp_score
        # print(mnn)
        # print(onn)





