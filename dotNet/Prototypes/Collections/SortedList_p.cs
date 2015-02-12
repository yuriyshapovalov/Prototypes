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

            Console.WriteLine("Clonning list 1 to list 2");
            var list1 = (SortedList) list.Clone();

            Console.Write("Elements in SortedList: ");
            foreach (DictionaryEntry element in list)
            {
                Console.Write("{{ {0}, {1} }} ", element.Key, element.Value);
            }
            Console.Write("\n");

            Console.WriteLine("Does cloned list contain key 3: {0}", list.Contains(3).ToString());

            Console.WriteLine("Added 5 elements: {0}", list.Count);
            list.Clear();
	    }
    }
}
