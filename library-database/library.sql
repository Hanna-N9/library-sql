CREATE TABLE typelist
(
  typelistid SERIAL PRIMARY KEY,
  typelistbook text not null,
  typelistdvd text not null,
  typelistcd text not null
);


CREATE TABLE author
 (
  authorid SERIAL PRIMARY KEY,
  authorfirstname text not null,
  authorlastname text not null
);


CREATE TABLE format 
(
  formatid SERIAL PRIMARY KEY,
  typelistid INTEGER REFERENCES typelist(typelistid),
  formattitle text not null,
  formatISBN numeric not null,
  authorid INTEGER REFERENCES author(authorid),
  formatcheckout text not null,
  formatduedate date not null
);


CREATE TABLE record
 (
  recordid SERIAL PRIMARY KEY,
  recordmembership text not null,
  formatID  INTEGER REFERENCES format(formatid),
  recordfees numeric not null,
  recordhistory text not null,
  memberrecord text not null
);


CREATE TABLE "member"
 (
  memberid SERIAL PRIMARY KEY,
  memberfirstname text not null,
  memberlastname text not null,
  memberemail text not null,
  address text not null,
  city text not null,
  "state" text not null,
  postalcode text not null,
  recordid INTEGER REFERENCES record(recordid)
);

CREATE TABLE membercard
 (
  membercardid SERIAL PRIMARY KEY,
  memberid INTEGER REFERENCES member(memberid),
  membercardtitle text not null,
  membercardnumber numeric not null,
  membercardexpiration date not null
);


CREATE TABLE status
(
  statusid SERIAL PRIMARY KEY,
  memberid INTEGER REFERENCES format(formatid),
  statussearch text not null,
  statusloan text not null,
  statusreturn text not null,
  statusorder numeric not null,
  statusfeesconfirmation  text not null,
  membercardid INTEGER REFERENCES membercard(membercardid)
);

CREATE TABLE librarian
(
  librarianid SERIAL PRIMARY KEY,
  librarianfirstname text not null,
  librarianlastname text not null,
  librarianemail text not null,
  librarianposition text not null,
  statusid INTEGER REFERENCES status(statusid)
);



CREATE TABLE door
 (
  doorid SERIAL PRIMARY KEY,
  doorroomnumber numeric not null,
  doorpinnumbers numeric not null
);


CREATE TABLE keycard 
(
  keycardid SERIAL PRIMARY KEY,
  librarianid INTEGER REFERENCES librarian(librarianid),
  doorid INTEGER REFERENCES door(doorid),
  keycarddatestart date not null,
  keycarddateend date not null
);


CREATE TABLE librariancard 
(
  librariancardid SERIAL PRIMARY KEY,
  librarianid INTEGER REFERENCES librarian(librarianid),
  librariancardnumber numeric not null
);


