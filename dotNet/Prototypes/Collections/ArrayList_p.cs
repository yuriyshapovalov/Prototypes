using System;
using System.Collections;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Collections
{
    class ArrayList_p
    {
        private ArrayList arrayList;

        public ArrayList_p()
        {
            arrayList = new ArrayList();

            Console.WriteLine("ArrayList default capacity: {0}", arrayList.Capacity);

            arrayList.Add("some");
            arrayList.Add("text");

            Console.WriteLine("ArrayList capacity (after adding 2 elements): {0}", arrayList.Capacity);

            arrayList.Add("foo");
            arrayList.Add("bar");
            arrayList.Add("lol");

            Console.WriteLine("ArrayList capacity (after adding 3 elements): {0}", arrayList.Capacity);
            Console.WriteLine("ArrayList count elements: {0}", arrayList.Count);


        }
    }
}
