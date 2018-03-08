import device_info_client
import multiprocessing
import card_rechage_manager
import time

def main_test():
    thread_list=[]
    T1=multiprocessing.Process(target=card_rechage_manager.main_v2,args=('oppo','MEmu_2','127.0.0.1:21523','com.zlongame.fs.nearme.gamecenter/com.amazing.flex.GameActivity'))
    T2=multiprocessing.Process(target=card_rechage_manager.main_v2,args=('oppo','MEmu_1','127.0.0.1:21513','com.zlongame.fs.nearme.gamecenter/com.amazing.flex.GameActivity'))
    #T3=multiprocessing.Process(target=card_rechage_manager.main_v2,args=('oppo','MEmu_3','127.0.0.1:21533','com.zlongame.fs.nearme.gamecenter/com.amazing.flex.GameActivity'))
   # T4=multiprocessing.Process(target=card_rechage_manager.main_v2,args=('oppo','MEmu_4','127.0.0.1:21543','com.zlongame.fs.nearme.gamecenter/com.amazing.flex.GameActivity'))
   # T5=multiprocessing.Process(target=card_rechage_manager.main_v2,args=('oppo','MEmu_5','127.0.0.1:21553','com.zlongame.fs.nearme.gamecenter/com.amazing.flex.GameActivity'))

    # T1=multiprocessing.Process(target=device_info_client.main,args=('13621480978','MEmu','127.0.0.1:21503'))
    # T2=multiprocessing.Process(target=device_info_client.main,args=('13136294648','MEmu_1','127.0.0.1:21513'))
        
    thread_list.append(T1)
    thread_list.append(T2)
    #thread_list.append(T3)
   # thread_list.append(T4)
   # thread_list.append(T5)

    for t in thread_list:

        t.start()

# def monkey_test():
#     T1=multiprocessing.Process(target=card_rechage_manager.main,args=('vivo','MEmu','127.0.0.1:21503','com.zulong.jz.vivo/com.zulong.jztkc.ZLPlayerActivity'))
#     T2=multiprocessing.Process(target=card_rechage_manager.main,args=('vivo','MEmu_1','127.0.0.1:21513','com.zulong.jz.vivo/com.zulong.jztkc.ZLPlayerActivity'))
#     thread_list.append(T1)
#     thread_list.append(T2)
#     for t in main_test():

#         t.start()    

if __name__ == '__main__':
    while card_rechage_manager.get_all_job('oppo')>0:

        device_info_client.close_device()
        main_test()

        print("The number of CPU is:" + str(multiprocessing.cpu_count()))
        while 1:
            time.sleep(3)
            print "all active_children:" ,multiprocessing.active_children()
            if len(multiprocessing.active_children())==0:
                break
        for p in multiprocessing.active_children():
            print("child   p.name:" + p.name + "\tp.id" + str(p.pid))
        print "END!!!!!!!!!!!!!!!!!"
