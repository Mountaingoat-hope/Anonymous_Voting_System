create table Auth(
      name text,
      username text,
      id serial primary key,
      pw text,
      gender varchar(1),
      dob date
      );
      
insert into Auth(name,username,pw) values ('Green','user1','user1');
