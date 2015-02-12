using System;
using System.Collections;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Collections
{
    // http://msdn.microsoft.com/ru-ru/library/system.collections.queue%28v=vs.110%29.aspx
    class Queue_p
    {
        public Queue_p()
        {
            Queue q = new Queue();

            q.Enqueue(1);
            q.Enqueue(4);
            q.Enqueue(3);

            Console.WriteLine("Queue count after 3 element enqueued: {0}", q.Count);
            Console.WriteLine("Is queue synchronized by default : {0}", q.IsSynchronized);

            Console.WriteLine("Is queue contains key 3 : {0}", q.Contains(3));

            Console.WriteLine("Dequeued element: {0}", q.Dequeue().ToString());

            Console.WriteLine("Peek element (does not delete from queue) : {0}", q.Peek().ToString());
        }
    }
}
