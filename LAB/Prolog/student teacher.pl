% STUDENT - TEACHEstudent_details(rahul).R - SUBJECT CODE DATABASE

% Student(Name, SubjectCode)
student(rahul, cs101).
student(priya, ec102).
student(arun, cs101).
student(divya, me103).

% Teacher(Name, SubjectCode)
teacher(ramesh, cs101).
teacher(suresh, ec102).
teacher(kumar, me103).

% Subject(SubjectName, SubjectCode)
subject(programming, cs101).
subject(electronics, ec102).
subject(mechanics, me103).

% Display complete details of a student
student_details(Student) :-
    student(Student, Code),
    subject(Subject, Code),
    teacher(Teacher, Code),
    write('Student Name  : '), write(Student), nl,
    write('Subject Code  : '), write(Code), nl,
    write('Subject Name  : '), write(Subject), nl,
    write('Teacher Name  : '), write(Teacher), nl.
% TEACHER FULL DETAILS

teacher_details(Teacher) :-
    teacher(Teacher, Code),
    subject(Subject, Code),
    write('Teacher Name : '), write(Teacher), nl,
    write('Subject Code : '), write(Code), nl,
    write('Subject Name : '), write(Subject), nl.
% SUBJECT FULL DETAILS

subject_details(Subject) :-
    subject(Subject, Code),
    write('Subject Name : '), write(Subject), nl,
    write('Subject Code : '), write(Code), nl.
% SUBJECT DETAILS USING SUBJECT CODE

subject_code_details(Code) :-
    subject(Subject, Code),
    write('Subject Code : '), write(Code), nl,
    write('Subject Name : '), write(Subject), nl.

%SUBJECT DETAILS USING SUBJECT CODE
subject_code_details(Code) :-
    subject(Subject, Code),
    teacher(Teacher, Code),
    write('Subject Name : '), write(Subject), nl,
    write('Subject Code : '), write(Code), nl,
    write('Teacher Name : '), write(Teacher), nl,
    write('Student Name : '),
    findall(Student, student(Student, Code), Students),
    write(Students), nl.
