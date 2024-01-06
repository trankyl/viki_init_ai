// Reconnaissane poids sensation entre n-gramme
using Brain4FuncApp;
using Brain4FuncApp.BlackBoard;
using Newtonsoft.Json;
using System.Diagnostics;

namespace narpoidssensengram
{
    class Program
    {

          static string lsbus_queue_input_memory_na_action = "";
           static  string lsbus_queue_input_memory_all_knowledge_source = "all_knowledge_source_input_memory";


          
        static void Main(string[] args)
        {
            string lprecondition = "using System;";

                var lliste_ngramme = Brain.lister_n_gramme(lprecondition);

                int lindex_n_gramme = 0;

                foreach(string lngram12 in lliste_ngramme)
                {
                 if (string.IsNullOrEmpty(lngram12)) continue;

                foreach(string lngram13 in lliste_ngramme)
                {
                 if (lngram12 == lngram13) continue;



                }        


                }        

        }
    }
}