from django.shortcuts import render
from .models import *
from random import *
from django.core.mail import send_mail
from hrms.models import *
# Create your views here.
def indexpage(request):
    if 'email' in request.session:
        uid = Add_Emoployess.objects.get(email=request.session['email'])
        return render(request,'hrms_employee/index.html',{'uid':uid})
    else:
        return render(request,'hrms_employee/login.html')

def login(request):
    if 'email' in request.session:
        uid = Add_Emoployess.objects.get(email=request.session['email'])
        return render(request,'hrms_employee/index.html',{'uid':uid})
    else:
        return render(request,'hrms_employee/login.html')        


def login_employee(request):
    try:
        if 'email' in request.session:
            # print("--------------------------->",request.session.id)
            # print("--------------------------->",request.session.email)
            # print("--------------------------->",request.session.firstname)
            uid = Add_Emoployess.objects.get(email=request.session['email'])
            return render(request,'hrms_employee/index.html',{'uid':uid})
        else:    
            email = request.POST['email']
            password = request.POST['password']
            uid = Add_Emoployess.objects.get(email=email)
            if uid:
                # print('-------------------------',uid)
                if uid.password == password:
                    request.session['email']=uid.email
                    request.session['id']=uid.id
                    # print("----------------------->",uid.id)
                    request.session['firstname']=uid.firstname
                    return render(request,'hrms_employee/index.html',{'uid':uid})
                else:
                    e_msg = "Password Is Wrong"    
                    return render(request,'hrms_employee/login.html',{'e_msg':e_msg})
            else:
                e_msg="You do not have authority to access this page" 
                return render(request,'hrms_employee/login.html',{'e_msg':e_msg})       
    except: 
        e_msg="User Does Not Exist"   
        return render(request,'hrms_employee/login.html',{'e_msg':e_msg})        


def forgot_password(request):
    return render(request,'hrms_employee/forgot-password.html')
        

def send_otp(request):
    try:
        email = request.POST['email']
        uid = Add_Emoployess.objects.get(email=email)
        if uid:
            n_otp = randint(1111,9999)
            uid.otp = n_otp
            uid.save()
            # send_mail('Your otp is'+str(n_otp),'try again','khushipatel284@gmail.com',[email],)
            return render(request,'hrms_employee/otp.html',{'email':email})
        else:
            e_msg = "user does not exist !!"
            return render(request,'hrms_employee/forgot-password.html',{'e_msg':e_msg})     
    except:    
        return render(request,'hrms_employee/forgot-password.html')


def otp(request):
    try:
        email = request.POST['email']
        otp1 = request.POST['otp1']
        otp2 = request.POST['otp2']
        otp3 = request.POST['otp3']
        otp4 = request.POST['otp4']
        otp = int(str(otp1)+str(otp2)+str(otp3)+str(otp4))
        # print('===========================',otp1)
        # print('===========================',otp2)
        # print('===========================',otp3)
        # print('===========================',otp4)
        # print('==============================',otp)
        uid = Add_Emoployess.objects.get(email=email)
        if uid:
            # print('============================',uid)
            if str(uid.otp)==str(otp):
                return render(request,'hrms_employee/change-password.html',{'uid':uid})
            else:
                e_msg ="you have entered a wrong otp"
                return render(request,'hrms_employee/otp.html',{'e_msg':e_msg})     
    except: 
        e_msg="User Not Valid"   
        return render(request,'hrms_employee/otp.html',{'e_msg':e_msg})


def chnage_password(request):
    try:
        email = request.POST['email']
        uid = Add_Emoployess.objects.get(email=email)
        newpassword = request.POST['newpassword']
        repassword = request.POST['repassword']
        if uid:
            # print('=============================',uid)
            if newpassword==repassword:
                uid.password=newpassword
                uid.save()
                return render(request,'hrms_employee/login.html')
            else:
                e_msg="password and confirm password doesn't match"    
                return render(request,'hrms_employee/change-password.html',{'e_msg':e_msg})
    except:
        return render(request,'hrms_employee/change-password.html')        


def profile(request):
    if 'email' in request.session:
        uid = Add_Emoployess.objects.get(email=request.session['email'])
        return render(request,'hrms_employee/profile.html',{'uid':uid})

def e_profile(request):        
    if 'email' in request.session:
        uid = Add_Emoployess.objects.get(email=request.session['email'])
        return render(request,'hrms_employee/edit_profile.html',{'uid':uid})

def edit_profile(request):
    if 'email' in request.session:
        if 'profile_pic' in request.FILES:
            profile_pic = request.FILES['profile_pic']  
            uid = Add_Emoployess.objects.get(email=request.session['email'])
            address = request.POST['address']
            birthdate = request.POST['birthdate']
            gender = request.POST['gender']
            pincode = request.POST['pincode']
            country = request.POST['country']
            state = request.POST['state']

            passport_number = request.POST['passport_number']
            passport_ex_date = request.POST['passport_ex_date']
            nationality = request.POST['nationality']
            religion = request.POST['religion']
            marital_status = request.POST['marital_status']
            child = request.POST['child']

            name = request.POST['name']
            relationship = request.POST['relationship']
            dob = request.POST['dob']
            mobile = request.POST['mobile']

            institute = request.POST['institute']
            subject = request.POST['subject']
            startind_date = request.POST['startind_date']
            complete_date = request.POST['complete_date']
            degree = request.POST['degree']
            grade = request.POST['grade']

            c_name = request.POST['c_name']
            location = request.POST['location']
            position = request.POST['position']
            p_from = request.POST['p_from']
            p_to = request.POST['p_to']

            bank_name = request.POST['bank_name']
            acc_num = request.POST['acc_num']
            ifsc = request.POST['ifsc']
            pan_no = request.POST['pan_no']

            uid.profile_pic=profile_pic
            uid.address=address
            uid.birthdate=birthdate
            uid.gender=gender
            uid.pincode=pincode
            uid.country=country
            uid.state=state
            uid.passport_number=passport_number
            uid.passport_ex_date=passport_ex_date
            uid.nationality=nationality
            uid.religion=religion
            uid.marital_status=marital_status
            uid.child=child
            uid.name=name
            uid.relationship=relationship
            uid.dob=dob
            uid.mobile=mobile
            uid.institute=institute
            uid.subject=subject
            uid.startind_date=startind_date
            uid.complete_date=complete_date
            uid.degree=degree
            uid.grade=grade
            uid.c_name=c_name
            uid.location=location
            uid.position=position
            uid.p_from=p_from
            uid.p_to=p_to
            uid.bank_name=bank_name
            uid.acc_num=acc_num
            uid.ifsc=ifsc
            uid.pan_no=pan_no
            uid.save()
            print('==================================successfully inserted')
            s_msg="Updated Profile Successfully"
            return render(request,'hrms_employee/profile.html',{'uid':uid})

        else:
            uid = Add_Emoployess.objects.get(email=request.session['email'])
            address = request.POST['address']
            birthdate = request.POST['birthdate']
            gender = request.POST['gender']
            pincode = request.POST['pincode']
            country = request.POST['country']
            state = request.POST['state']

            passport_number = request.POST['passport_number']
            passport_ex_date = request.POST['passport_ex_date']
            nationality = request.POST['nationality']
            religion = request.POST['religion']
            marital_status = request.POST['marital_status']
            child = request.POST['child']

            name = request.POST['name']
            relationship = request.POST['relationship']
            dob = request.POST['dob']
            mobile = request.POST['mobile']

            institute = request.POST['institute']
            subject = request.POST['subject']
            startind_date = request.POST['startind_date']
            complete_date = request.POST['complete_date']
            degree = request.POST['degree']
            grade = request.POST['grade']

            c_name = request.POST['c_name']
            location = request.POST['location']
            position = request.POST['position']
            p_from = request.POST['p_from']
            p_to = request.POST['p_to']

            bank_name = request.POST['bank_name']
            acc_num = request.POST['acc_num']
            ifsc = request.POST['ifsc']
            pan_no = request.POST['pan_no']
            
            uid.address=address
            uid.birthdate=birthdate
            uid.gender=gender
            uid.pincode=pincode
            uid.country=country
            uid.state=state
            uid.passport_number=passport_number
            uid.passport_ex_date=passport_ex_date
            uid.nationality=nationality
            uid.religion=religion
            uid.marital_status=marital_status
            uid.child=child
            uid.name=name
            uid.relationship=relationship
            uid.dob=dob
            uid.mobile=mobile
            uid.institute=institute
            uid.subject=subject
            uid.startind_date=startind_date
            uid.complete_date=complete_date
            uid.degree=degree
            uid.grade=grade
            uid.c_name=c_name
            uid.location=location
            uid.position=position
            uid.p_from=p_from
            uid.p_to=p_to
            uid.bank_name=bank_name
            uid.acc_num=acc_num
            uid.ifsc=ifsc
            uid.pan_no=pan_no
            uid.save()
            print('==================================successfully inserted')
            s_msg="Updated Profile Successfully"
            return render(request,'hrms_employee/profile.html',{'uid':uid})
    else:
        return render(request,'hrms_employee/profile.html',{'uid':uid})
           


def e_logout(request):
    if 'email' in request.session:
        del request.session['id']
        del request.session['email']
        del request.session['firstname']
        s_msg = "Sign Out Successfully"
        return render(request,'hrms_employee/login.html',{'s_msg':s_msg})
    else:
        s_msg = "Sign Out Successfully"
        return render(request,'hrms_employee/login.html',{'s_msg':s_msg})


def ticket(request):
    data = Ticket.objects.all()  
    if data:
        for i in data:
            print('===============',i.id)
    if 'email' in request.session:
        uid = Add_Emoployess.objects.get(email=request.session['email'])
        return render(request,'hrms_employee/tickets.html',{'data':data})  

       

def ticket_open(request):
    try:
        if 'email' in request.session:
            uid = Add_Emoployess.objects.get(email=request.session['email']) 
            subject = request.POST['subject']
            ticket_id = request.POST['ticket_id']
            assign_staff = request.POST['assign_staff']
            client = request.POST['client']
            priority = request.POST['priority']
            cc = request.POST['cc']
            assign = request.POST['assign']
            followers = request.POST['followers']
            description = request.POST['description']
            file = request.FILES['file'] 
            insert = Ticket.objects.create(uid=uid,subject=subject,ticket_id=ticket_id,assign_staff=assign_staff,client=client,priority=priority,cc=cc,assign=assign,followers=followers,description=description,file=file)
            if insert:
                return render(request,'hrms_employee/tickets.html',{'insert':insert})    
    except:
        return render(request,'hrms_employee/tickets.html')  

def ticket_edit(request):
    try:
        if 'email' in request.session:
            uid=Add_Emoployess.objects.get(email=request.session['email'])

        id = request.POST['id']
        uid1 = Ticket.objects.get(id=id)
        if uid1:
            print('====================',uid1)
            subject = request.POST['subject']
            ticket_id = request.POST['ticket_id']
            assign_staff = request.POST['assign_staff']
            client = request.POST['client']
            priority = request.POST['priority']
            cc = request.POST['cc']
            assign = request.POST['assign']
            followers = request.POST['followers']
            description = request.POST['description']
            file = request.FILES['file']
            uid1.subject=subject
            uid1.ticket_id=ticket_id
            uid1.assign_staff=assign_staff
            uid1.client=client
            uid1.priority=priority
            uid1.cc=cc
            uid1.assign=assign
            uid1.followers=followers
            uid1.description=description
            uid1.file=file
            uid1.save()
            print('=========================updated')
            return render(request,'hrms_employee/tickets.html')
    except:            
            return render(request,'hrms_employee/tickets.html')
        