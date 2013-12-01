using System;
using System.Collections;

namespace Collections
{
    class SortedList_p
    {
        SortedList list;
        public SortedList_p ()
	    {
            list = new SortedList();

            Console.WriteLine("SortedList dafault capacity: {0}", list.Capacity);

            list.Add(2, "some");
            list.Add(3, "text");
            list.Add(1, "hello");
            list.Add(4, "world");
            list.Add(5, "bar");

            Console.WriteLine("Added 5 elements: {0}", list.Count);
            Console.WriteLine("SortedList current capacity: {0}", list.Capacity);

	    }
    }
}
