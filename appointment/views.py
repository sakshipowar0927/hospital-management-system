
from django.shortcuts import render, redirect
from functools import wraps

from .models import doctor, appointment, patient


# ================= LOGIN REQUIRED DECORATOR =================

def login_required_session(view_func):

    @wraps(view_func)
    def wrapper(request, *args, **kwargs):

        if not request.session.get('is_logged_in'):
            return redirect('login')

        return view_func(request, *args, **kwargs)

    return wrapper


# ================= LOGIN =================

def login_page(request):

    if request.session.get('is_logged_in'):
        return redirect('app_home')

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        if username == "admin" and password == "soft":

            request.session.cycle_key()
            request.session['is_logged_in'] = True

            return redirect("app_home")

        else:
            return render(request, "login.html", {
                "error": "Invalid username or password"
            })

    return render(request, "login.html")


# ================= HOME =================

@login_required_session
def home(request):
    return render(request, "app_home.html")


# ================= ABOUT =================

def about(request):
    return render(request, "about.html")


# ================= LOGOUT =================

def logout_page(request):
    request.session.flush()
    return redirect("login")


# ================= APPOINTMENT =================

@login_required_session
def appointment_show(request):

    appointments = appointment.objects.all()

    return render(request, 'appointment_show.html', {
        "appointments": appointments
    })


@login_required_session
def appointment_insert(request):

    if request.method == "POST":

        pnm = request.POST.get("pnm")
        dnm = request.POST.get("dn")
        t = request.POST.get("t")
        d = request.POST.get("d")
        c = request.POST.get("c")

        appointment.objects.create(
            pnm=pnm,
            dnm=dnm,
            t=t,
            d=d,
            c=c
        )

        return redirect("appointment_show")

    doctors = doctor.objects.all()
    patients = patient.objects.all()

    return render(request, 'appointment_insert.html', {
        "doctors": doctors,
        "patients": patients
    })


@login_required_session
def appointment_update(request, aid):

    appointments = appointment.objects.get(aid=aid)

    if request.method == "POST":

        appointments.pnm = request.POST.get("pnm")
        appointments.dnm = request.POST.get("dn")
        appointments.t = request.POST.get("t")
        appointments.d = request.POST.get("d")
        appointments.c = request.POST.get("c")

        appointments.save()

        return redirect("appointment_show")

    doctors = doctor.objects.all()
    patients = patient.objects.all()

    return render(request, "appointment_update.html", {
        "appointment": appointments,
        "doctors": doctors,
        "patients": patients
    })


@login_required_session
def appointment_delete(request, aid):

    appointments = appointment.objects.get(aid=aid)
    appointments.delete()

    return redirect("appointment_show")


# ================= DOCTOR =================

@login_required_session
def doctor_show(request):

    doctors = doctor.objects.all()

    return render(request, "doctor_show.html", {
        "doctors": doctors
    })


@login_required_session
def doctor_insert(request):

    if request.method == "POST":

        dn = request.POST.get("dn")
        sp = request.POST.get("sp")
        dcon = request.POST.get("dcon")
        e = request.POST.get("e")

        doctor.objects.create(
            dn=dn,
            sp=sp,
            dcon=dcon,
            e=e
        )

        return redirect("doctor_show")

    return render(request, "doctor_insert.html")


@login_required_session
def doctor_update(request, did):

    doctors = doctor.objects.get(did=did)

    if request.method == "POST":

        doctors.dn = request.POST.get("dn")
        doctors.sp = request.POST.get("sp")
        doctors.dcon = request.POST.get("dcon")
        doctors.e = request.POST.get("e")

        doctors.save()

        return redirect("doctor_show")

    return render(request, "doctor_update.html", {
        "doctor": doctors
    })


@login_required_session
def doctor_delete(request, did):

    doctors = doctor.objects.get(did=did)
    doctors.delete()

    return redirect("doctor_show")


# ================= PATIENT =================

@login_required_session
def patient_show(request):

    patients = patient.objects.all()

    return render(request, "patient_show.html", {
        "patients": patients
    })


@login_required_session
def patient_insert(request):

    if request.method == "POST":

        pnm = request.POST.get("pnm")
        con = request.POST.get("con")
        a = request.POST.get("a")
        m = request.POST.get("m")

        patient.objects.create(
            pnm=pnm,
            con=con,
            a=a,
            m=m
        )

        return redirect("patient_show")

    return render(request, "patient_insert.html")


@login_required_session
def patient_update(request, pid):

    patients = patient.objects.get(pid=pid)

    if request.method == "POST":

        patients.pnm = request.POST.get("pnm")
        patients.con = request.POST.get("con")
        patients.a = request.POST.get("a")
        patients.m = request.POST.get("m")

        patients.save()

        return redirect("patient_show")

    return render(request, "patient_update.html", {
        "patient": patients
    })


@login_required_session
def patient_delete(request, pid):

    patients = patient.objects.get(pid=pid)
    patients.delete()

    return redirect("patient_show")
