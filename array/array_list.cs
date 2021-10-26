var arlist1 = new ArrayList();

var arlist2 = new ArrayList()
                    {
                        1, "Bill", " ", true, 4.5, null
                    };

int[] arr = { 100, 200, 300, 400 };

Queue myQ = new Queue();
myQ.Enqueue("Hello");
myQ.Enqueue("World!");

arlist1.AddRange(arlist2); //adding arraylist in arraylist 
arlist1.AddRange(arr); //adding array in arraylist 
arlist1.AddRange(myQ); //adding Queue in arraylist 
