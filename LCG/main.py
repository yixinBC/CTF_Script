import sympy
import libnum
import contextlib


def lcg_get_m(output):
    t = [output[i] - output[i - 1] for i in range(1, len(output))]
    return [int(sympy.gcd(t[i + 3] * t[i + 1] - t[i + 2] * t[i + 2], t[i + 2] * t[i] - t[i + 1] * t[i + 1])) for i in range(len(t) - 3)]

def lcg_get_a(output, m):
    lis = []
    with contextlib.suppress(Exception):
        lis.extend((output[i + 2] - output[1]) * int(sympy.mod_inverse((output[i + 1] - output[i]), m)) % m for i in range(len(output) - 2))
    return lis

def lcg_get_b(output, a, m):
    return [(output[i] - a * output[i-1]) % m for i in range(1, len(output))]

def lcg_get_seed(output, a, b, m):
    with contextlib.suppress(Exception):
        a_inv = int(sympy.mod_inverse(a, m))
        return a_inv * (output[0] - b) % m

def lcg_solver(output, isPrint=True, isSet=False):
    lis = []
    for m in lcg_get_m(output):
        for a in lcg_get_a(output, m):
            for b in lcg_get_b(output, a, m):
                if (seed := lcg_get_seed(output, a, b, m)):
                    lis.append(seed)

    if isSet:
        lis = list(set(lis))
            
    if isPrint:
        for seed in lis:
            print(libnum.n2s(seed))
    return lis

if __name__ == '__main__':
    # output = [69676071514199964129368494511049773706185789519381885090989836826032423348931601761005255484444660094, 63031206989830671133688676504767396390656004885395484175664501826753686622909142758317354395992301026, 10982611756211554291222567868588733322082261620905115629089850311461024570081479382334755302093076626, 57593354371133571326881703280620102147253648139230630688131873856129105654575862207035367081838844484, 47619980490914264678052844656879066638030284466312631649629134306776942962249639156106765582151143844, 58789571370633161248337888914950971131623915440268354523313877777336488371785773275506162258821825516, 109481456137357201661490538198304522268006931099085677213764961347749368305449034788701532872386412243, 19307804703479426044115964742461201656670909298595515226324824508728816047217841799764422041962083267, 93700801968408201834162526077717334683725582703626747502836611244942102316238114344746715776427713387, 87095688282213954059983741940081650190732077925687511841367934545528486899471711188785929150582606959]
    output = [2362956263554848170817729987754611374928204274967748213482967526790646738692550494632686977605208124188164, 1272774410874317473670489174711151283842765704668789171057284003611511386277261507754750964030540471223565, 898982732342703863320991923205294587525869915431666895395350261011619733544248006834659710572114326635176, 2605108648366962409362647341634151151683570377790751041905577827369955936068519953780810763065590026709642, 2085998239792031891546268826259052653103310188786564909648386799865874059000264433415887678375234055781183, 1056062457012308922306581668219464282750217942037759606849987545327693824327814341037476841440815564079798, 2182504276869403618999593972078608895262196338036377015932439255627231434754913125255610612534092646605520, 1554748322991028777460381298766095073857639296646112762830350768614445020765763227681814150496693495044250, 2307915444185938322547554797556246210645139214659075550407575285577333700932965549465126134842440885654676, 411068882836855649055582443155224381449420676041100704621993277452694400824923872344461663651348379143917]
    lcg_solver(output, isPrint=True, isSet=False)
    