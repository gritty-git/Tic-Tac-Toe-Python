import random
ctr=0
c='i'
fl=0
ty=1
comp=int(1)
board=[0,1,2,3,4,5,6,7,8]
corner=[0,2,6,8]
done=[]
mv="NULL"

        
def draw():
    print("draw heigala re pena")
def status():
    print("""
                    {} | {} | {}
                    ------------
                    {} | {} | {}
                    ------------
                    {} | {} | {}
                    """.format(board[0],board[1],board[2],board[3],board[4],board[5],board[6],board[7],board[8]))
    global ctr
    ctr+=1
def display_instruct():
    """Display game instructions."""  
    print(
    """
    Welcome to the greatest intellectual challenge of all time: Tic-Tac-Toe.  
    This will be a showdown between your human brain and my silicon processor.

    Rs.10/- re khelantu ei jhakas game au hareiki dekhantu mo computer ku....
    hareidele mu apananku debi Rs.10/- ra treat :-)!!!

    You will make your move known by entering a number, 0 - 8.  The number 
    will correspond to the board position as illustrated:
    
                    0 | 1 | 2
                    ---------
                    3 | 4 | 5
                    ---------
                    6 | 7 | 8
                    NOTE
                    NOTE
                    NOTE:Human->o
                         Computer->x

    Prepare yourself, human.  The ultimate battle is about to begin. \n
    """
    )
def win_check():
    status()
    global ctr
    global fl
    
    if (board[1]==board[2]==board[0] or board[5]==board[4]==board[3] or board[6]==board[7]==board[8] or board[0]==board[3]==board[6] or board[1]==board[4]==board[7] or board[8]==board[2]==board[5] or board[8]==board[2]==board[5] or board[8]==board[4]==board[0] or board[6]==board[2]==board[4]): 
           
            fl=1
            if c=='y':
                print("you won")
            elif c=='n':
                print("chii....chii...dhik to jibana,computer tharu harigalu")
    elif (ctr>=8):
        fl=1
        print("draw heigala")    
def hum_move():
    ty=1
    print("enter your choice")
    while ty==1:
        
       mv=int(input())
       if mv in done:
           
           print("bhala choice paka")
       else:
            ty=1
            done.append(mv)
            board[int(mv)]='o'
            break
def comp_move():
    tuk=0
    qwer=0
    cot=0
    ty=1
    while ty==1:
        for i in range(9):
             if i not in done:
                 
                    tuk=board[i]
                    board[i]='x'
                    
                    if (board[1]==board[2]==board[0] or board[5]==board[4]==board[3] or board[6]==board[7]==board[8] or board[0]==board[3]==board[6] or board[1]==board[4]==board[7] or board[8]==board[2]==board[5] or board[8]==board[2]==board[5] or board[8]==board[4]==board[0] or board[6]==board[2]==board[4]): 
                        print("computer entered(computer jitila) ",i)
                        done.append(i)
                        cot=1
                        break
                    else:
                       board[i]=tuk
                    
                    tuk=board[i]
                    board[i]='o'
                    
                    if (board[1]==board[2]==board[0] or board[5]==board[4]==board[3] or board[6]==board[7]==board[8] or board[0]==board[3]==board[6] or board[1]==board[4]==board[7] or board[8]==board[2]==board[5] or board[8]==board[2]==board[5] or board[8]==board[4]==board[0] or board[6]==board[2]==board[4]): 
                        print("computer entered(tate jiteilani) ",i)
                        board[i]='x'
                        done.append(i)
                        cot=1
                        break
                    else:
                       board[i]=tuk   

        if cot==1:
            break


        if ((board[0]=='o' and board[4]=='x' and board[8]=='o') or (board[2]=='o' and board[4]=='x' and board[6]=='o')):
            done.append(1)
            board[int(1)]='x'
            print("computer entered ",1)
            break

        
        elif cot==0:
            for j in corner:
                if j not in done:
                    done.append(j)
                    board[int(j)]='x'
                    print("computer entered ",j)
                    qwer=1
                    break
                
        
            
        if (qwer==1 or cot==1):
            break
        
                
        mv=random.randint(0,8)
        if mv in done:
                ty=1
        else:
                done.append(mv)
                board[int(mv)]='x'
                print("computer entered ",mv)
                break
        

def main():
    global ctr
    display_instruct()
    print("first chance nabu:y/n")
    global c
    c=input()
    if c=='y':
        hum_move()
        if board[0]=='o':
            done.append(4)
            board[4]='x'
            print("computer entered ",4)
            c='n'
        elif board[2]=='o':
            done.append(4)
            board[4]='x'
            print("computer entered ",4)
            c='n'
        elif board[6]=='o':
            done.append(4)
            board[4]='x'
            print("computer entered ",4)
            c='n'
        elif board[8]=='o':
            done.append(4)
            board[4]='x'
            print("computer entered ",4)
            c='n'
            
            
    elif c=='n':
        comp_move()
    else:
        print("kain pena bhali hauchu.... jetiki option deichi setikiru choose karunu")
    status()    
    while (fl==0):
            if c=='n':
                hum_move()
                c='y'
                win_check()
                if (fl=='1'):
                    print("gf")
                    break
                
            elif c=='y':
                comp_move()
                c='n'
                win_check()
                
                
   
main()    
input("enter daba nahele chadibini")

