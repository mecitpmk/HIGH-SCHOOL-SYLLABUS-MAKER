from list_dict import *
import random
from tkinter import *
import sys
# print(sys.getrecursionlimit())
# sys.setrecursionlimit(5000)
# print(sys.getrecursionlimit())
class GUI(Frame):
    def __init__(self,parent):
        self.parent = parent
        Frame.__init__(self, parent)
        self.initGUI()
        self.grid()
    def initGUI(self):
        BIG_TEXT = Label(self,text="HIGH SCHOOL AUTO SYLLABUS MAKER",bg="green",fg="white",anchor=CENTER).grid(row=0,column=0,columnspan=3,padx=10,pady=10,sticky=E+W+S+N)
        
        self.CL_FRAME = Frame(self,relief=GROOVE,borderwidth=4)
        self.CL_FRAME.grid(row=1,column=0,columnspan=2,padx=10,pady=10)
        CLASSR = Label(self.CL_FRAME, text="CLASSROOM->EX(12-A)").grid(row=1,column=1,padx=10,pady=10,sticky=E)
        self.ClassRoomEntries = Entry(self.CL_FRAME)
        self.ClassRoomEntries.grid(row=1,column=2,padx=10,pady=10,sticky=W)

        self.createClassRoomBut = Button(self.CL_FRAME,text="Create ClassRoom!", command = self.create_classroom)
        self.createClassRoomBut.grid(row=1,column=3,padx=10,pady=10,columnspan=2,sticky=E+W+S+N)

        self.TC_FRAME = Frame(self,relief=GROOVE,borderwidth=4)
        self.TC_FRAME.grid(row=2,column=0,columnspan=2,padx=10,pady=10)

        T_NAME = Label(self.TC_FRAME, text="Teacher Name").grid(row=2,column=0 , sticky=E,padx=10,pady=10)
        
        self.teacher_Name_Ent = Entry(self.TC_FRAME)
        self.teacher_Name_Ent.grid(row=2,column=1,padx=10,pady=10,sticky=W)

        T_BRUNCH = Label(self.TC_FRAME, text="Teacher Brunch").grid(row=2,column=2, sticky=E,padx=10,pady=10)
        self.teacher_brunch_Ent = Entry(self.TC_FRAME)
        self.teacher_brunch_Ent.grid(row=2,column=3,padx=10,pady=10,sticky=W)

        T_MAX_OV = Label(self.TC_FRAME, text="Teacher Max Overloads:").grid(row=2,column=4,sticky=E,padx=10,pady=10)
        self.teacher_max_loads = Entry(self.TC_FRAME)
        self.teacher_max_loads.grid(row=2,column=5,padx=10,pady=10,sticky=W)

        self.create_Teacher = Button(self.TC_FRAME,text="Create Teacher",command=self.create_Teach)
        self.create_Teacher.grid(row=3,column=2,padx=10,pady=10,columnspan=2,sticky=E+W+S+N)
        
        self.viewFeatures = Frame(self,relief=GROOVE, borderwidth=4)
        self.viewFeatures.grid(row=3,column=0,columnspan=2, padx=10,pady=10)

        CREATED_CR = Label(self.viewFeatures,text="↓Created ClassRooms↓").grid(row=0,column=0,padx=40,pady=10)

        CREATED_TC = Label(self.viewFeatures,text="↓Created Teachers↓").grid(row=0,column=1,padx=40,pady=10)

        self.classrListbox = Listbox(self.viewFeatures)
        self.classrListbox.grid(row=1,column=0,padx=40,pady=10)
        self.classrListbox.bind("<Double-Button>",self.get_classroom_infos)


        self.teacherListbox = Listbox(self.viewFeatures)
        self.teacherListbox.grid(row=1,column=1,padx=40,pady=10)
        self.teacherListbox.bind("<Double-Button>",self.get_teacher_infos)


        self.ShuffleBut = Button(self.viewFeatures,text="Make Syllabus!",command=self.make_shuffle)
        self.ShuffleBut.grid(row=2,column=0,columnspan=2, padx=10,pady=10,sticky=E+W+S+N)

    def get_classroom_infos(self,event):
        self.capture_classr = event.widget
        self.current_classr  = self.capture_classr.curselection()
        self.current_classr  = self.classrListbox.get(self.current_classr)
        self.current_classr_obj  = ClassRoom.all_dict[self.current_classr]
        # print(current_classr_obj.days,current_classr_obj.days['Monday'].clocks[9])
        self.current_class_toplv = Toplevel(self)
        self.current_class_toplv.title(string=self.current_classr_obj.room_name)
        
        Label(self.current_class_toplv,text = "Lessons ",bg="green",fg="white").grid(row=0,column=0,padx=10,pady=10,sticky=E+W+S+N,columnspan=3)
       
        row,col = 1,0
        
        Fr = Frame(self.current_class_toplv) 
        Fr.grid(row=row,column=col,padx=10,pady=10,sticky=E+W+S+N)
        Label(Fr,text="Lesson Name",fg="blue").grid(row=row,column=col,padx=10,pady=10)
        Label(Fr,text="Lesson Hour",fg="blue").grid(row=row,column=col+1,padx=10,pady=10,)
        Label(Fr,text="Lesson Teacher",fg="blue").grid(row=row,column=col+2,padx=10,pady=10)
        for l_Name , l_Obj in self.current_classr_obj.lessons.items():
            if l_Obj.lesson_teacher  == None:
                current_bg = "red"
            else:
                current_bg = "green"
            
            MyFrame = Frame(self.current_class_toplv,relief=GROOVE,borderwidth=2,bg=current_bg)
            MyFrame.grid(row=row+1,column=col, padx=10,pady=10,sticky=E+W+S+N)

            T_FR  = Frame(MyFrame,bg=current_bg)
            T_FR.grid(row=row,column=col,padx=10,pady=10,sticky=E+W+S+N)

            T_FR2  = Frame(MyFrame,bg=current_bg)
            T_FR2.grid(row=row,column=col+1,padx=10,pady=10,sticky=E+W+S+N)
            
            T_FR3  = Frame(MyFrame,bg=current_bg)
            T_FR3.grid(row=row,column=col+2,padx=10,pady=10,sticky=E+W+S+N)
            
            Label(T_FR,text=l_Obj.lesson_name,bg=current_bg,anchor=CENTER).grid(row=row,column=col,sticky=E+W+S+N)
            Label(T_FR2,text=f'\t{l_Obj.lesson_hour}',bg=current_bg,anchor=CENTER).grid(row=row,column=col+1,sticky=E+W+S+N)
            Label(T_FR3,text=f'\t{l_Obj.lesson_teacher}',bg=current_bg,anchor=CENTER).grid(row=row,column=col+2,sticky=E+W+S+N)
            row+=1
        self.SEESYLLABUS = Button(self.current_class_toplv,text="See ClassRoom's Syllabus",command=self.SYLBS)
        self.SEESYLLABUS.grid(row=row+1,column=col,padx=10,pady=10,sticky=E+W+S+N)
        
    def SYLBS(self):
        new_topl = Toplevel(self.current_class_toplv)
        new_topl.title(string=self.current_classr_obj.room_name)
        r,c = 0,1
        other_row = 1
        new_label_dict = {}
        Label(new_topl,text="Clocks",bg="aqua").grid(row=0,column=0,padx=10,pady=10,ipadx=12)
        for days in ClassRoom.days_list:
            Label(new_topl,text=days,bg="green").grid(row=r,column=c,padx=10,pady=10,ipadx=10)
            other_row = 1
            for a in range(9,17):
                X = Label(new_topl,text="",bg="yellow",width=10)
                X.grid(row=other_row,column=c,padx=3,pady=3)
                print(other_row,c)
                new_label_dict.setdefault(days,{})
                new_label_dict[days][a] = X
                other_row+=1
            c+=1
        print(new_label_dict)
        
        rowx,columnx=1,0
        for a in range(9,17):
            Label(new_topl,text=f'{a}:00-{a+1}:00',bg="aqua").grid(row=rowx,column=columnx,padx=10,pady=10,ipadx=10)
            rowx+=1
        

        for day in self.current_classr_obj.days:
            for clocks,objects in day.clocks.items():
                # print(day,clocks,objects)
                if objects != None:
                    new_label_dict[day.day_name][clocks].configure(text=objects,bg="red",fg="white")
                

    def get_teacher_infos(self,event):
        self.capture_teach = event.widget
        self.current_teach  = self.capture_teach.curselection()
        self.current_teach  = self.teacherListbox.get(self.current_teach)
        current_teach_obj  = Teacher.all_dict[self.current_teach]

        self.current_t_toplv = Toplevel(self)

        self.T_INFO = Label(self.current_t_toplv,text="Teacher Informations",bg="green",fg="white")
        self.T_INFO.grid(row=0,column=0,padx=10,pady=10,columnspan=3,sticky=E+W+S+N)
        

        Label(self.current_t_toplv,text="↓Teacher Taking ClassRooms↓").grid(row=1,column=0,padx=10,pady=10)

        lb_courses =  Listbox(self.current_t_toplv)
        lb_courses.grid(row=2,column=0,padx=10,pady=10)
        lb_courses.bind("<Double-Button>",self.get_classroom_infos)
        
        for taked in current_teach_obj.taking_classrooms:
            lb_courses.insert(END,taked)

        new_Fr  = Frame(self.current_t_toplv,relief=GROOVE,borderwidth=3)
        new_Fr.grid(row=1,column=1,padx=25,pady=10,rowspan=2)

        Label(new_Fr, text=f"Teacher Name : {current_teach_obj.teacher_name}").grid(row=0,column=0,padx=10,pady=10)
        Label(new_Fr,text=f'Teacher Brunch : {current_teach_obj.brunch}').grid(row=1,column=0,padx=10,pady=10)
        self.m_WL_LBL = Label(new_Fr,text=f'Max Workloads : {current_teach_obj.max_workloads}')
        self.m_WL_LBL.grid(row=2,column=0,padx=10,pady=10)
        Label(new_Fr, text=f'Loaded Workloads: {current_teach_obj.current_loads}').grid(row=3,column=0,padx=10,pady=10)
        self.ChangeMaxW = Button(new_Fr,text="Change Max Workloads",command=self.changeWL)
        self.ChangeMaxW.grid(row=4,column=0,padx=10,pady=10,sticky=E+W+S+N)
        self.changeWL_OBJ = current_teach_obj
    def changeWL(self):
        
        newF = Frame(self.current_t_toplv,relief=GROOVE,borderwidth=3)
        newF.grid(row=1,column=2,padx=25,pady=10,rowspan=2)

        self.old_WLL=Label(newF,text=f"Old Max Workloads:{self.changeWL_OBJ.max_workloads}")
        self.old_WLL.grid(row=0,column=0,padx=10,pady=10,columnspan=2)
        
        self.new_w_E = Entry(newF)
        self.new_w_E.grid(row=1,column=0,padx=10,pady=10)

        ch_but = Button(newF,text="Change Now!",command=self.chNow)
        ch_but.grid(row=1,column=1,padx=10,pady=10)

    def chNow(self):
        if self.new_w_E.get() != "":
            try:
                self.changeWL_OBJ.max_workloads = int(self.new_w_E.get())
            except:
                print("Should Be Integer!")
            else:
                print("Completed")
                self.old_WLL.config(text=f"Old Max Workloads:{self.changeWL_OBJ.max_workloads}")
                self.m_WL_LBL.configure(text=f'Max Workloads : {self.changeWL_OBJ.max_workloads}')
                self.colorful_thins()
    def make_shuffle(self):
        system_obj = System()
        system_obj.run()
        self.colorful_thins()
    def colorful_thins(self):
        print("*******************-****************")
        for index , obj in enumerate(self.teacherListbox.get(0,END)):
            for t_ob in Teacher.all_list:
                if t_ob.__repr__() == obj:
                    if t_ob.max_workloads == t_ob.current_loads:
                        self.teacherListbox.itemconfig(index,bg='red')
                    elif t_ob.current_loads == 0:
                        self.teacherListbox.itemconfig(index,bg="green")
                    else:
                        self.teacherListbox.itemconfig(index,bg="yellow")
        for index, obj in enumerate(self.classrListbox.get(0,END)):
            for cl_obj in ClassRoom.all_list:
                if cl_obj.__repr__() == obj:
                    if cl_obj.total_lessons_num == cl_obj.taken_lessons:
                        self.classrListbox.itemconfig(index,bg="red")
                    elif cl_obj.taken_lessons == 0:
                        self.classrListbox.itemconfig(index, bg ="green")
                    else : 
                        self.classrListbox.itemconfig(index,bg = "yellow")
        
    def create_Teach(self):
        if self.teacher_brunch_Ent.get() != "" and self.teacher_Name_Ent.get() != "" and self.teacher_max_loads != "":
            if self.teacher_Name_Ent.get() not in Teacher.all_dict:
                self.teacherListbox.insert(END,Teacher(teacher_name=self.teacher_Name_Ent.get(),
                                                            brunch=self.teacher_brunch_Ent.get(),
                                                            max_workloads=int(self.teacher_max_loads.get())))
                print("Teacher Created")


    def create_classroom(self):
        if self.ClassRoomEntries.get() != "":
            if ClassRoom.all_dict.get(self.ClassRoomEntries.get()) == None:
                self.classrListbox.insert(END,ClassRoom(self.ClassRoomEntries.get()))
                print("ClassRoom Created...")

class Lesson:
    def __init__(self,lesson_name,lesson_hour,lesson_teacher=None):
        self.lesson_name=lesson_name
        self.lesson_hour=lesson_hour
        self.lesson_teacher=lesson_teacher
        self.taked = 0
    def __repr__(self):
        return self.lesson_name

class Clocks:
    def __init__(self,day_name):
        self.day_name = day_name
        self.clocks={}
        for a in range(9,17):
            self.clocks.setdefault(a,None)
        self.start = 9
        self.finish = 16
    def __repr__(self):
        return self.day_name
    

class ClassRoom:
    all_dict = MyDict()
    all_list = MyList()
    taken_lessons=0
    days_list = ["Monday","Tuesday","Wednesday","Thursday","Friday"]
    def __init__(self,room_name):
        self.fish_dict =  {  
                "9":{'Mathematics':Lesson('Mathematics',4),
                    'Physics':Lesson('Physics',4),
                    'Chemistry':Lesson('Chemistry',4)},
                "10":{'Mathematics':Lesson('Mathematics',4),
                    'Physics':Lesson('Physics',4),
                    'Chemistry':Lesson('Chemistry',4)},
                "11":{'Mathematics':Lesson('Mathematics',6),
                    'Physics':Lesson('Physics',6),
                    'Chemistry':Lesson('Chemistry',4)},
                "12":{'Mathematics':Lesson('Mathematics',6),
                    'Physics':Lesson('Physics',6),
                    'Chemistry':Lesson('Chemistry',4)}}
        self.days = [Clocks(day_name = a) for a in self.days_list]
        self.room_name= room_name
        self.teachers_list = MyList()
        self.fishman = (self.room_name.split("-")[0])
        self.lessons = self.fish_dict[self.fishman]
        self.total_lessons_num  = len(self.lessons)
        self.completed_week_plan= []
        ClassRoom.all_dict[self.room_name] = self
        ClassRoom.all_list.append(self)
        
    def __repr__(self):
        return self.room_name

class Teacher:
    all_dict = MyDict()
    all_list = MyList()
    current_loads = 0
    def __init__(self,teacher_name,brunch,max_workloads=30):
        self.teacher_name = teacher_name
        self.brunch=brunch
        self.max_workloads = max_workloads
        self.taking_classrooms = []
        Teacher.all_dict[self.teacher_name] = self
        Teacher.all_list.append(self)
    def teacher_taking(self,given_lessons):
        if given_lessons in self.taking_classrooms:
            return True
        else:
            if self.current_loads < self.max_workloads and (given_lessons.lessons[self.brunch].lesson_hour+self.current_loads) <= self.max_workloads:
                return False
            elif self.current_loads >= self.max_workloads:
                return True
            else:
                return True
    def __repr__(self):
        return self.teacher_name

class System:
    def run(self):
        self.available_brunch = set()
        for t in Teacher.all_list:
            self.available_brunch.add(t.brunch)
        self.recursive_funct()
        for obj in ClassRoom.all_list:
            for b in obj.lessons:
                print(obj , b , obj.lessons[b].lesson_teacher)

        self.not_did = ClassRoom.all_list.copy()
        print(self.not_did)

    
        self.recursive_funct2()

        for day_obj in ClassRoom.all_list:
            dayx_obj = day_obj.days
            print("*************-----",day_obj,"--------*********")
            for days_obj in dayx_obj:
                
                print(days_obj.day_name , days_obj.clocks)
                print("*****************************************")
        
    
    def recursive_funct2(self,param=None):
        # try:
        if len(self.not_did) == 0:
            return True
        else:
            if param is None:
                self.random_class = random.choice(self.not_did) #rastegele seçilmiş sınıf objesi
            else:
                self.random_class = param
            self.random_classes_lessons = self.random_class.lessons # rastege seçilmiş sınıf objesinin dersleri (DİCTİONARY)

            self.rand_list_les = [self.random_classes_lessons[a] for a in self.random_classes_lessons if self.random_classes_lessons[a].lesson_teacher != None \
                                                    and self.random_classes_lessons[a] not in self.random_class.completed_week_plan] # rastele DERSLER listesi
            if len(self.rand_list_les) == 0:
                return True
            
            self.random_choice_lesson  = random.choice(self.rand_list_les) # RASTGELE SEÇİLEN DERS OBJESI
            
            self.random_day_obj = [a for a in self.random_class.days if not all(a.clocks.values())]
            
            self.random_day_obj = random.choice(self.random_class.days)  # RASTGELE SEÇİLEN GÜN OBJESI
            
            self.rand_list_clck = [a for a in self.random_day_obj.clocks if self.random_day_obj.clocks[a] == None]
            
            self.random_clock = random.choice(self.rand_list_clck) # RASTGELE SEÇİLEN SAAT

            if self.check_completed(given_class = self.random_class):
                self.not_did.remove(self.random_class)
                return self.recursive_funct2()
            else:
                test_list = MyList()
                Check_Completed = []
                for other_rooms in ClassRoom.all_list:
                    if other_rooms == self.random_class:
                        continue
                    else:
                        for d in other_rooms.days:
                            if d.day_name == self.random_day_obj.day_name:
                                if self.random_clock == 16:
                                    if d.clocks[self.random_clock] != None and d.clocks[self.random_clock-1] != None:
                                        test_list.append_args(d.clocks[self.random_clock-1].lesson_teacher == self.random_choice_lesson.lesson_teacher,
                                                        d.clocks[self.random_clock].lesson_teacher == self.random_choice_lesson.lesson_teacher)
                                else:
                                    if d.clocks[self.random_clock] != None and d.clocks[self.random_clock+1] != None:
                                        test_list.append_args(d.clocks[self.random_clock].lesson_teacher == self.random_choice_lesson.lesson_teacher,d.clocks[self.random_clock+1].lesson_teacher == self.random_choice_lesson.lesson_teacher)
                                    else:
                                        if d.clocks[self.random_clock] != None:
                                            test_list.append_args(d.clocks[self.random_clock].lesson_teacher == self.random_choice_lesson.lesson_teacher)
                                        if d.clocks[self.random_clock+1] != None:
                                            test_list.append_args(d.clocks[self.random_clock+1].lesson_teacher == self.random_choice_lesson.lesson_teacher)
                               
                counter = 0
                other_counter = 0
                for test in self.random_day_obj.clocks.values():
                    if test == self.random_choice_lesson:
                        other_counter +=1
                

                for d_o in self.random_class.days:
                    for cl,obj in d_o.clocks.items():
                        if obj != None:
                            if obj == self.random_choice_lesson:
                                counter+=1
                
                if other_counter == 2:
                    # print("Aynı Gun 2 den Fazla dERS OLAMAZ!")
                    self.recursive_funct2(self.random_class)
                elif counter == self.random_choice_lesson.lesson_hour:
                    # print("Credit Limit")
                    self.random_class.completed_week_plan.append(self.random_choice_lesson)
                    if self.check_completed(self.random_class):
                        self.recursive_funct2()
                    else:
                        return self.recursive_funct2(self.random_class)
                elif any(test_list):
                    print(test_list)
                    # print("Same Course in Same Clocks IDENTIFIED!!")
                    if self.check_completed(self.random_class):
                        self.recursive_funct2()
                    else:
                        return self.recursive_funct2(self.random_class)
                else:
                    if self.random_clock == 9 and self.random_day_obj.clocks[self.random_clock] == None and self.random_day_obj.clocks[self.random_clock+1] == None:
                        self.random_day_obj.clocks[self.random_clock] = self.random_choice_lesson
                        self.random_day_obj.clocks[self.random_clock+1] = self.random_choice_lesson
                    elif self.random_clock == 16 and self.random_day_obj.clocks[self.random_clock] == None and self.random_day_obj.clocks[self.random_clock-1] == None:
                        self.random_day_obj.clocks[self.random_clock] = self.random_choice_lesson
                        self.random_day_obj.clocks[self.random_clock-1] = self.random_choice_lesson
                    elif self.random_day_obj.clocks[self.random_clock] == None:
                        if self.random_clock != 16:
                            if self.random_day_obj.clocks[self.random_clock+1] == None: 
                                self.random_day_obj.clocks[self.random_clock] = self.random_choice_lesson
                                self.random_day_obj.clocks[self.random_clock+1] = self.random_choice_lesson
                    if self.check_completed(given_class = self.random_class):
                        self.not_did.remove(self.random_class)
                        self.recursive_funct2()
                    else:
                        self.recursive_funct2(self.random_class)


    def check_completed(self,given_class):
        lesson_dicts = {}
        for days_object in given_class.days:
            for clocks,lesson_obj in days_object.clocks.items():
                if lesson_obj in lesson_dicts:
                    lesson_dicts[lesson_obj]+=1
                else:
                    if lesson_obj != None:
                        lesson_dicts.setdefault(lesson_obj,1)
    

        lenght=0
        completed=0
        for lesson,lessons in given_class.lessons.items():
            if lessons.lesson_teacher != None:
                lenght+=1
            if lessons in lesson_dicts:
                if lesson_dicts[lessons] == lessons.lesson_hour:
                    completed+=1
        if completed  == lenght:
            print(completed,lenght,lesson_dicts,True)
            return True
        else:
            print(completed,lenght,lesson_dicts,False)
            return False

    def recursive_funct(self):
        try:
            ct = 0
            for available_b in self.available_brunch:
                for les in ClassRoom.all_list:
                    if les.lessons[available_b].lesson_teacher != None:
                        ct+=1
            if len(ClassRoom.all_list) * len(self.available_brunch) == ct:
                return True
            
            teacher_first = random.choice(Teacher.all_list)
            first_class = random.choice(ClassRoom.all_list)
            
            if teacher_first.max_workloads == teacher_first.current_loads:
                self.recursive_funct()
            else:
                print(first_class)
                if (not teacher_first.teacher_taking(given_lessons = first_class)) and first_class.lessons[teacher_first.brunch].lesson_teacher == None:
                    print("Teacher Can Take This Course")
                    teacher_first.taking_classrooms.append(first_class)
                    first_class.lessons[teacher_first.brunch].lesson_teacher = teacher_first
                    teacher_first.current_loads+=first_class.lessons[teacher_first.brunch].lesson_hour
                    first_class.taken_lessons+=1
                    self.recursive_funct()
                else:
                    self.recursive_funct()
        except :
            return False        
            

def main():

    root = Tk()
    create_gui  = GUI(root)
    root.title("Syllabus Program")
    root.mainloop()

if __name__ == "__main__":
    main()
