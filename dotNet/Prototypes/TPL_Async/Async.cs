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
            var web = new WebClient();
            var web2 = new WebClient();

            Task<string> googleTask = Task<string>.Factory.StartNew(() => { 
                return web.DownloadString("http://google.com");
            });

            googleTask.ContinueWith(t => {

                Console.WriteLine(googleTask.Result);
            });

            Task<string> yandexTask = web2.DownloadStringTaskAsync("http://yandex.ru");

            Console.WriteLine(yandexTask.Result);

            Thread.Sleep(10000);

            Console.ReadKey();
        }
    }
}
