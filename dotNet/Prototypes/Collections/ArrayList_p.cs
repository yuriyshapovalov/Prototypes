using System;
using System.Collections;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Collections
{
    // http://msdn.microsoft.com/ru-ru/library/system.collections.arraylist%28v=vs.110%29.aspx
    class ArrayList_p
    {
        private ArrayList arrayList;
        private ArrayList arrayList1;

        public ArrayList_p()
        {
            arrayList = new ArrayList();
            arrayList1 = new ArrayList(40);

            Console.WriteLine("ArrayList default capacity: {0}", arrayList.Capacity);
            Console.WriteLine("ArrayList(40) default capacity: {0}", arrayList1.Capacity);

            arrayList.Add("some");
            arrayList.Add("text");

            Console.WriteLine("ArrayList capacity (after adding 2 elements): {0}", arrayList.Capacity);

            arrayList.Add("foo");
            arrayList.Add("bar");
            arrayList.Add("lol");

            Console.WriteLine("ArrayList capacity (after adding 3 elements): {0}", arrayList.Capacity);
            Console.WriteLine("ArrayList count elements: {0}", arrayList.Count);

            Console.WriteLine("ArrayList has a fixed size: {0}", arrayList.IsFixedSize);
            Console.WriteLine("ArrayList is read-only: {0}", arrayList.IsReadOnly);
            Console.WriteLine("ArrayList is synchronized (thread-safe): {0}", arrayList.IsSynchronized);

            var s_arrList = ArrayList.Synchronized(arrayList);

            Console.WriteLine("ArrayList is synchronized (thread-safe): {0}", s_arrList.IsSynchronized);

            lock (arrayList.SyncRoot)
            {
                foreach (var element in arrayList)
                { 
                    Console.Write("{0} ", element.ToString());
                }
                Console.Write("\n");
            }

            // ArrayList does not guarantee sorted array, need to sort in manually before doing BinarySearch
            arrayList.Sort();
            int elementIndex = arrayList.BinarySearch("foo");
            Console.WriteLine("ArrayList BinarySearch returns element position: {0}", elementIndex.ToString());

            arrayList.TrimToSize();
            Console.WriteLine("ArrayList capacity after trimming to size: {0}", arrayList.Capacity);

            arrayList.Clear();
            Console.WriteLine("ArrayList count after clearing: {0}", arrayList.Count);
            Console.WriteLine("ArrayList capacity after clearing: {0}", arrayList.Capacity);

        }
    }
}
