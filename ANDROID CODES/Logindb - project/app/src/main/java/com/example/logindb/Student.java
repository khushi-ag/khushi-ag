package com.example.logindb;

public class Student {

    String id,fname,lname,midname,yr,month,dt;

    public Student(String id, String fname, String lname, String midname, String yr, String month, String dt) {
        this.id = id;
        this.fname = fname;
        this.lname = lname;
        this.midname = midname;
        this.yr = yr;
        this.month = month;
        this.dt = dt;
    }

    public Student() {
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getFname() {
        return fname;
    }

    public void setFname(String fname) {
        this.fname = fname;
    }

    public String getLname() {
        return lname;
    }

    public void setLname(String lname) {
        this.lname = lname;
    }

    public String getMidname() {
        return midname;
    }

    public void setMidname(String midname) {
        this.midname = midname;
    }

    public String getYr() {
        return yr;
    }

    public void setYr(String yr) {
        this.yr = yr;
    }

    public String getMonth() {
        return month;
    }

    public void setMonth(String month) {
        this.month = month;
    }

    public String getDt() {
        return dt;
    }

    public void setDt(String dt) {
        this.dt = dt;
    }

    @Override
    public String toString() {
        return "Student{" +
                "id='" + id + '\'' +
                ", fname='" + fname + '\'' +
                ", lname='" + lname + '\'' +
                ", midname='" + midname + '\'' +
                ", yr='" + yr + '\'' +
                ", month='" + month + '\'' +
                ", dt='" + dt + '\'' +
                '}';
    }
}
