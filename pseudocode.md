OBJECTIVES

Create the backend to a todo list
Make it alterable
Access it and add/delete items from it
Make sure the list, the user and the categories are all connected
Make some events that can also be listed/created by the user

FUNCTIONALITY

- User able to add todos to the list
    - User able to give a label to each todo (its name) - not null - char limited
    - User able to give a description to each todo (what is actually to be done) - null - char limited
    - User able to choose a category type for each todo (created by user and then becoming a choice unless new)
    - User able to choose a priority for each todo
    - User able to see the comlpeted status of the todo, who created it, when it was created and when it is due

- User able to add events to an events list
    - User able to see the events, their date and who created them
    - User able to change if an event has happened or not

#################################################

Table users as U {
  id int [pk, increment] //from T.priority
  name varchar [default:"admin"] //[fk] 1:many
  //uses admin to start but connects to created_by
}
//-----------------------------------
Table todos as T {
  id int [pk, increment]
  label varchar [not null]
  description varchar [null]
  priority choice [default:'low'] // [fk] to U.id many:1 
  completed boolean [default: False] //[fk] to C.completed 1:1
  created_by varchar [default:'admin'] // from users
  created_at datetime [default:'date']
  due_by datetime [default:'date'] //[fk] to C.due 1:1
  category choice [default:'daily'] //[fk] to C.type 1:1
 }
//-----------------------------------
Table categories as C {
  id int [pk, increment]
  user_id int [default:null] // [fk] from U.id 1:1
  label choice [default:'daily'] // from T.category 1:1
}
//-----------------------------------
Table events as E {
  id int [pk, increment]
  name varchar [not null]
  start datetime [default:'date']
  end datetime [default:'date']
  description varchar [not null]
  status varchar [not null]
  created_by varchar [not null] // from users
}
//-----------------------------------
Ref: T.priority > U.id // many:1
Ref: T.id > U.id // many:many
Ref: U.id > T.created_by // 1:many
Ref: T.category > C.id // 1:1
Ref: U.id > E.created_by // 1:many
Ref: U.id > C.user_id //1:1
