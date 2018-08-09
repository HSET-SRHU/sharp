============================
SHARP Application Change Log
============================

Change #1
=========

**Description:**
              that the indentation is removed.
**Controller and Function:**
              dlsklsd

**Model:**
              sdksld

**Other:**
              dsldksd
                  
**Code Changes:**

.. code-block:: python
   :linenos:
                  import datetime
                  import math
                  def index(): return dict(message="hello from Project_List.py")


                  @auth.requires_login()
                  def All_Projects():
                      gridanchor =A(SPAN(_class='glyphicon glyphicon-paperclip')+
                      ('Grid View'),_href=URL('Projects','List_Projects'),_class='btn btn-info') or ''
                      if (request.vars.myprojects == 'myprojects'):
                         var_heading= 'My'
                         query = (db.Projects.Name_of_PI == auth.user_id)

                      elif request.vars.Project_Status == 'tobecompleted':
                          today = datetime.date.today()
                          last_monday     = today - datetime.timedelta(days=today.weekday())
                          next_week_saturday= last_monday + datetime.timedelta(weeks=2) + datetime.timedelta(days=5)
                          if auth.has_membership('admin'):
                              var_heading=request.vars.Project_Status
                              query = ((db.Projects.End_Date <= next_week_saturday)&(db.Projects.Project_Status == 'In Progress'))
                          else:
                              var_heading=request.vars.Project_Status
                              query = ((db.Projects.End_Date <= next_week_saturday)&
                              (db.Projects.Project_Status == 'In Progress')&(db.Projects.Name_of_PI == auth.user_id))

                      else:
                          query = (db.Projects)
                          var_heading='All'
                      counts=db(query).count()
                      userquery=query
                      rows=db(query).select()
                      projects = DIV(' ',_id=0,_class='grid')
                      i =1
                      divid='PROJECT '
                      for row in rows:

**Date:**
            08/12/12


