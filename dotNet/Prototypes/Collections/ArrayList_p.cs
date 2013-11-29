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

            arrayList.Add("some text");

            Console.WriteLine("ArrayList default capacity: {0}", arrayList.Capacity);
        }
    }
}
