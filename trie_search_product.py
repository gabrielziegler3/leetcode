from collections import defaultdict
from typing import *


class TrieNode:
    def __init__(self):
        self.children = {}
        self.words = []


class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.search_result = []

    def insert(self, word):
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node.words.append(word)
            node = node.children[char]

    def search_prefix(self, prefix):
        node = self.root

        for idx, char in enumerate(prefix):
            if char not in node.children:
                self.search_result.append(list())
            else:
                results = sorted(
                    [
                        word
                        for word in node.words
                        if (0 <= idx < len(prefix))
                        and idx < len(word)
                        and word[idx] == prefix[idx]
                    ]
                )[:3]
                self.search_result.append(results)
                node = node.children[char]
        return self.search_result


class Solution:
    def suggestedProducts(
        self, products: List[str], searchWord: str
    ) -> List[List[str]]:
        trie = Trie()
        for product in products:
            trie.insert(product)

        return trie.search_prefix(searchWord)


products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
searchWord = "mouse"
res = Solution().suggestedProducts(products, searchWord)
from pprint import pprint

pprint(res)

products = ["havana"]
searchWord = "tatiana"
res = Solution().suggestedProducts(products, searchWord)
from pprint import pprint

pprint(res)

products = [
    "jhljdwmzajzhbzlnuvnzlypvdwelzenkmuekbfhhwrfgltwxtytyeifurnnvdjyzwzsqyprcqxatrfvfabwoeoybqfbtkgicltqtkzgdvpwsnzvvhgelwqqtdruknthexbnznixtpktmxlxadnnjuzynvmcajkcopefw",
    "e",
    "jhljdwmzajzhbzlnuvnzlypvdwelzenkmuekbfhhwrfgltwxtytyeifurnnvdjyzwzsqyprcqxatrfvfabwoeoybqfbtkgicltqtkzgdvpwsnzvvhgelwqqtdruknthfmpgekmnsnxbjtgkorweyotixwlcwyvjhsgjmcxkthszqffcuanqe",
    "jhljdwmzajzhbzlnuvnzlypvdwelzenkmuekbfhhwrfgltwxtytrpopmqtztvx",
    "jhljdwmzajzhbzlnuvnzlypvdwelzenkmuekbfhhwrfgltwxtytyeifurnnvdjyzwzsqyprcqxqhqxshczwndevtdwdugkhjm",
    "jhljdwmzajzhbzlnuvnzlypvdwelzenkmuekbfhhwrfgltwxtytyeifurnnvdjyzwzsqyprcqxatrfvfabwoeoybqfbtkgicltqtkzgdvpwsnzvvttiblsecbwbjiavybqjbubhqsosblxhjlazg",
    "jhljdwmzajzhbzlnuvnzlypvdwelzenkmuekbfhhwrfgltwxtytyeifurnnvdjyzwzsqyprcqxatrfvfabwoeoybqfbtkgicltqtkzgdvpwsnzvvhgelwqqtdruknthfmpgekmnsnxbjtgkorweyotixwlcwyvjhsgjmcxkthszqffcuanghx",
    "jhljdwmzajzhbzlnuvnzlypvdwelzenkmuekbcrmqovcdmysuiwudydsgndjtflykmzfvoawkkargexytjuihnomiqezyqujqalafxxcg",
    "jhljdwmzajzhbzakqaljdrmlykjmnuxobohfrtkkfomnncrtyhnrmnktddhctwbmjdrbyewjtxlmvwwonjmurxatshntdvdmkyqmhsnjvykrydssnf",
    "jhljdwmzajzhbzlnuvnzlypvdwelzenkmuekbfhhwrfgltwxtytyeifurnnvdjyzwzsqyprcqxatrfvfabwoeoybqfbtkgicltcjueumbdovisfkvoiaefajnbyqrvddajklehucxgvwgwltqwrwtljigyazlxgmlubt",
    "jyutgoofzhfhohyrtjnggsyboyfvvseghifejwcdmvzlnbvqoitmikuayaqjf",
    "crkvwptcqpxixdxswlnbzqvegbkcrzyvqyfpivuqyvkwctpqxsvjzmdkxwkxrydzwdavrydzsenajijzxzruziraagmydnhukkpscglmgkjnslerwjwjiousltlcxpjqutgqwrfrzgyzdaxssjxqjvtqupmiqmjebsmwtkv",
    "sawxfkvjanqhwadpiftppejzh",
    "jhljdprevkydjfzuynjkmaxnljentqvjxxmkguoaxpefhss",
    "mrklrbtfxyyxkmreglnvsprvpcqeiabavruobchukroohjupgdfcid",
    "tnhgepglkwouzzzuirpzblbiqiupywjoenrzgtneawycsvrmnsnthtpixftlvrhjfoohkcjttpdnmtergskgcywrnkhqbdclj",
    "jhljdwmzajzhbzlnuvnzlypvdwelzenkmuekbfhhwrfgltwxtoqqwlufsrshrqebujsztrldskcxywiiunzpvqztigbhsnf",
    "jhljdwmzajzhbzlnuvnzlypvdwelzenkmuekbfhhwrfgltwxtytyeifurnnvdjyzwzsqyprcqxatrfvfabwoeoybqfbtkgicltqtkzgdvpwsnzvvhgelwqqtdruknthfmpgekmnsnxbjtgkorweyotixwlcwyvjhsgjmcxofu",
    "jemqslzvrbskvqvjwbivkxiwvzunyvyydicmnujacrzbomugingscfodfroyatsdwfbbktajyvbcwxusitnbbupjrjniemerrlujvfkbvzuzyysrunmwyftywgpybacbgvprybhhbymnc",
    "jhljdwmzajbejfyewkvhnpbenzedarvjstpywnqsrwbzrwsdiazferiliucjutqsriviycqgcycqgptbvxjpdmcszurlxynvjvlpmcsjvvuhwdwggxpkisfyjpgmunydqnkgdyvcycdcaeeqngkpqbuylneelpkmrtytqt",
    "jhljdwmzajzhbzlnuvnzlypvdwelzenkmuekbfhhwrfgltwxtytyeifurnnvdjyzmdgvq",
    "jhljdwmzajzhbzlnuvnzlypvdwelzenkmuekbfhhwrfglaovojaskdmlzqdcpljyogaghonmtqlmkheawtgjfjjfxwepamg",
    "jhljdwmzajzhbzlnuvnzlypvdwelzenkmuekbfhhwrfgltwxtytyeifurnnvdjyzwzsqyprcqxatrfvfabwoeoybqfbtkgicltqtkzgdvpwsnzvvhgelwqqtdruknthfmpgekmnsnxbjtgkorweyotixwlcwyvjhsgjmcxktgckdmdknsghw",
    "jhljdwmzajzhrugyiyhfobthuolttcxhbabkgztyewftchcgnbdlfklinalsnbisnbauhavkklbstnljdabxjxrlfpzcwdvwqbuelrnpxwfyxkbsuwqhhavxjilscwsejepgeagioyuygvzeaosdydemiuzlxrrymgiipmhlrroacigbirotx",
    "jhljdwmzajzhbzlnuvnzlypvdwelzenkmuekbfhhwrfgltwxtytyeifurnnvdjyzwzsqyprcqxatrfvfabwoeoybqfbtkgicltqtkzgdvpwsnzvvhgelwqqtdruneluwssmtwondnulmnmcric",
    "swtiutizdsgfqoouqpqnfnymxozrkmifylc",
    "qjkacgudpntqmnfjwajlvwflwujmzgumbmwnyxmidpxhjvbofutovdrxvsibvivvcpvahdlnvdpyrvkmqbodehmaos",
    "jhljdwmzajzhbzlnuvnzlypvdwelzenkmuekbfhhwrfgltwxtytyeifurnnvdjyzwzsqyprcqxatrfvfabwoeoybqfbtkgicltqtkhrfhyuqwrlprwdrztwncnfawbhmhizugfbykzjlmkorprcpmvaqnxollxjduplrpbpkoc",
    "jhljdwmzajzhbzlnuvnzlypvdwelzenkmuekbfhhwrfgltwxtytyeifurnnvdjylhkiabzfarxcdfmnazomofjjovszxwsajkgjnnqgqhxbzfzkczmqdargeklvqphngmf",
    "jhljdwmzajzhbzlnuvnzlypvdwelzenkmuekbfhhwrfgltwxtytyeifurnnvdjyzwzsqyprcqxatrfvfabwoeoybqfbtkgicltqtkzgdmglxthgqgkfdxwbhglifxgddbudyvzbstnzajtzxrwenpgxbbgnoopjlqmvksbrblqgpoau",
    "jhljdwmzajzhbzlnuvnzlypvdwelzenkmuekbfhhwrfgltwxtytyeifurnnvdjyzwzsqyprcqxatrfvfabwoeoybqfbtkgicltqtkzgdvpwsnzvvhgelwmgeapqviocqlwxhwdrspdnvfwsueyflaqyugnaiaudyebelavrmcinpegwdkvasq",
    "gmdipfdbrbpxtoguoczzylbvtwvkeizjzpkitxemlbpntgabfquceexutahhhtazajrvyebswsfcdmyzrbcuhbbomvfbigueneoxboixhmgadagvesvohhxikxpsgepomzrmgopjwcunqzweycsfzonuxjvseetopcwkqrxj",
    "jhljdwmzajzhbzlnuvnzlypvdwelzenkmuekbfhhwrfgltwxtytyeifurnnvdjyzwzsqyprcqxatrfvfabwoeoybqfbtkgicltqtkzgdvpwsnzvvhgelwqqtdruknthfmpgekymqswxnblzzdrsx",
    "jhljdwmzajzhbzlnuvnzlypvdwelzenkmuekbfhhwrfgltwxtyinanuoqxhrzpid",
    "wmdynsfqafmwakfzgmmjv",
    "geukdsnoidgngoaeutlenbeacbkwvfsnaxpjzwyfaaxtgpuagsyihiiukpcqruacvpztqpfzjkqedrgawldrwsvoeckpbaxiewvsxgwfrvxwjporwmsdzrfgxsvhqtshdpiwugahibdxwapqgct",
    "ksnkokylbndlrspqntlwkvzggnltumwgietvlntdtycnlfwtonlulrvkbwwalcbphlfyuklwaxepyykq",
    "jhljdwmzajzhbzlnuvnzlypvdwelzenkmuekbfhhwrfgltwxtytyeifurnnvdjyzwzsqyprcqxatrfvfabwoeoybqfbtkgicltqtkzgdvpwsnzvvhgelwqqtdrrsydhaggrspsxqxjyamfzdjijwkkzlilzetrbhoufyjtvt",
    "jhljdwmzajzhbzlnuvnzlypvdwelzenkmuekbfhhwrfgltwxtytyeifurnnvdjyskqujjuoyergkhjiuetyuqmxlbrhvqccdojfuvxapxxmttcvkyhpwhnswbn",
    "jhljdwmzajzhbzlnuvnzlypvdwelzenkmuekbfhhwrfgltwxtytyeifurnnvdjyzwzzgvnyvifeoconimcrvivomvcbxndlagodcreyjsujuujdtlggyqju",
    "jhljdwmzajzhbzlnuvnzlypvdwelzenkmuekbfhhwrfgltwxtytyeifurnnvdjyzwzsqyprcqxatrfvjslklhoywcnkynwmpcsxqmffltmxerhqhftrggsxbdjywazmbcipemgiuge",
    "jhljdwmzajzhbzlnuvnzlypvdwelzenkmuekbfhhwrfgltwxtytyeifurnnvdjyzwzsqyprcqxatrfvfabwoeoybqfbtkgicltqtkzgdvpwsnzvvhgelwqqtdruknthfmpgekmnsnxbjtgkorweyotixwlcwyvjhahpb",
    "pgfelbqsbxstdvbwzwclelbcfuskheuguwevadhynw",
    "mzkgksixdpjpjucbwcosbutjhqxbzrajlprvfyufivhsifkhqxzhskosssvazinljvqncpbibothtrmfkfrtxjgqvml",
    "jhljdwmzajzhbzlnuvnzlypvdwelzenkmuekbfhhwrfgltwxtytylppbjczpsuzbiyuddxnxcjumqrmswhtkssqxdbmjyqpznmtb",
    "jhljdwmzajzhbzlnuvnzlypvdwelzenkmuekbfhhwrfgltwxtytyeifurnnvdjyzwzsqyprcqxatrfvfabwoewiednmizszpecznfjvzgpkzmfkkavirmvzcosdzbtvlfbwbwwedxgpqcniqf",
    "jhljdwmzajzhbzlnuvnzlypvdwelzenkmuekbfhhwrfgltwxtytyeifurnnvdjyzwzsqyprcqxatrfvfabwoeoybqfbtkgicltqtkzgdvpwsnzvvhgelwqqtdruknthfmpgekmnsnxbjtgkorweyotixwlcwyvjhsgjmcxkthszqffcurmze",
    "kidvqciatjrmmwmgufyjdnfiznohewcegbdcklsrtxlrjpskyyihjydbsmacyrbjgihxbwruhuzlzgqmwyqosvgrtzelkcwkfettntncocivaavgnyodrshepkpbjy",
    "znzriimpzgugozuixpdsqyxcuqsuwwwenchyemscgjwmchlctkbtkdjcbkgswfwxr",
    "jhljdwmzajzhbzlnuvnzlypvdwelzenkmuekbfhhwrfgltwxtytyeifurnnvdjyzwzsqyprcqxatrfvfabwoeoybqfbtkgicltqtkhaeyrgeellxwuzdaa",
    "jhljdwmzajzhbzlnuvnzlypvdwelzenkmuekbfhhwrfgltwxtytyeifurnnvdjyzwzsqyprcqxatrfvfabwoeoybqfbtkgiclqgtjennjvmb",
    "jhljdwmzajzhbzlnuvnzlypvdwelzenkmuekbfhhwrfgltwxtytyeifurnnvdjyzwzsqyprrziwvgzuwpysmnkfo",
    "jhljdwmzajzhbzlnuvnzlypvdwelcnexkdfskoxkymborxnexhyctvminpdvdekwmokprwgskobsianemxeneuovowebrusncqutzhujgkswiovoialiqokiwkmbybbjbeenxarwoxbupustfxqgpivsawecebesdyfvsknvlnt",
    "jhljdwmzajzhbzlnuvnzlypvdwelzenkmuekbfhhwrfgltwxtytyeifurnnvdjyzwzsqyprcqxatrfvfafumkcmonskgyuaffuitlxqxeubifkawlkqfntkfxxjomjuffcdprwzwzpltnxaritqqdtnmuhndokxnphlhdygvfcifg",
    "jhljdwmzajzhbzlnuvnzlypvdwvlwblyfwchpsytymysowjgldscaabrrvzelklbcllnmpersjfezqmhhphq",
]
searchWord = "jhljdwmzajzhbzlnuvnzlypvdwelzenkmuekbfhhwrfgltwxtytyeifurnnvdjyzwzsqyprcqxatrfvfabwoeoybqfbtkgicltqtkzgdvpwsnzvvhgelwqqtdruknthfmpgekmnsnxbjtgkorweyotixwlcwyvjhsgjmcxkthszqffcuanggmjxvzykcfajvlbromoiaabgtihdkyxrfdlofvhsbdjlbyktpawxdwqgwlaxqjzdvvvvrksuhfuyjimkuiptxbkehzvgefavleaegbopivdhzpzhgehjorevmxvzivdigmldsrgtlptdorekere"
res = Solution().suggestedProducts(products, searchWord)
from pprint import pprint

pprint(res)
