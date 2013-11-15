using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

namespace TPL_Async
{
    class Async
    {
        static void Main(string[] args)
        {
            Thread dedicatedThread = new Thread(ComputeBoundOp);
            dedicatedThread.IsBackground = true;
            dedicatedThread.Start(5);
            Console.WriteLine("Main Thread, doing other work here.");
            Thread.Sleep(1000);

            dedicatedThread.Join();

            var web = new WebClient();
            var web2 = new WebClient();

            Task<string> googleTask = Task<string>.Factory.StartNew(() => { 
                return web.DownloadString("http://google.com");
            });

            googleTask.ContinueWith(t => {
                if (t.IsFaulted)
                {
                    Console.WriteLine("Resource not found");
                }
                else
                {
                    Console.WriteLine(googleTask.Result);
                }
            });

            Task<string> yandexTask = web2.DownloadStringTaskAsync("http://yandex.ru");


            Console.WriteLine(yandexTask.Result);

            Thread.Sleep(10000);

            Console.ReadKey();
        }

        private static void ComputeBoundOp(Object state)
        {
            Console.WriteLine("In compute bound state {0}", state);
            Thread.Sleep(1000);
        }
    }
}
