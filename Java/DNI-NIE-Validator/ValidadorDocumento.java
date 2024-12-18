package DNI-NIE-Validator;

import Entrada;

public class ValidadorDocumento {
    public static void main(String[] args) {
        System.out.println("Mete tu DNI/NIE:");
        String t = Entrada.cadena();
        if (correctoDNIoNIE(t)) {
            System.out.println("DNI/NIE CORRECTO: " + ensenarDNIoNIE(t));
        } else {
            System.out.println("Tu DNI o NIE es incorrecto.");
        }
    }

    private static boolean esDNIoNIE(String t) {
        return t.matches("[0-9]{8}[A-Z]") || t.matches("[XYZ][0-9]{7}[A-Z]"); // DEFINE SI ES UN POSIBLE DNI O NIE POR SU ESTRUCTURA
    }

    private static boolean esDNI(String t) {
        return t.matches("[0-9]{8}[A-Z]") && esDNIoNIE(t); // DEFINE SI ES DNI O NIE
    }

    private static boolean correctoDNIoNIE(String t) { // DEFINE SI LA LETRA DEL DNI O NIE ES CORRECTA
        t = t.toUpperCase().strip(); // PASA A MAYUSCULAS Y QUITA ESPACIOS
        String[] l = {"T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B", "N", "J", "Z", "S", "Q", "V", "H", "L", "C", "K", "E"};
        if (esDNI(t)) { // SI ES DNI, COMPRUEBA SU LETRA DE ESTA MANERA
            @SuppressWarnings("UnnecessaryTemporaryOnConversionFromString")
            int n = Integer.valueOf(t.substring(0, t.length() - 1));
            if ((n % 23) == (java.util.Arrays.asList(l).indexOf(t.substring(t.length() - 1)))) { // COMPRUEBA QUE LA ULTIMA LETRA COINCIDA CON LA DEL ARRAY
                return true; // LETRA DEL DNI CORRECTA
            }
        } else { // SI ES NIE, COMPRUEBA SU LETRA DE ESTA MANERA
            @SuppressWarnings("UnnecessaryTemporaryOnConversionFromString")
            int n = Integer.valueOf(t.substring(1, t.length() - 1)); // APARTA EL PRIMER Y ULTIMO CARACTER
            if (t.substring(0, 1).equals("Y")) { // SUSTITUYE LA Y POR UN 1
                n += 10000000;
            }
            if (t.substring(0, 1).equals("Z")) { // SUSTITUYE LA Z POR UN 2
                n += 20000000;
            }
            return ((n % 23) == (java.util.Arrays.asList(l).indexOf(t.substring(t.length() - 1)))); // LETRA DEL NIE CORRECTA
        }
        return false; // NO ES NI DNI NI NIE CORRECTO
    }

    private static String ensenarDNIoNIE(String t) { // DEVUELVE EL DNI O NIE NORMALIZADO
        t = t.toUpperCase().strip(); // PASA A MAYUSCULAS Y QUITA ESPACIOS
        if (correctoDNIoNIE(t)) {
            if (esDNI(t)) { // SI ES UN DNI CON MENOS DE 8 NUMEROS, AÑADE 0'S A LA IZQUIERDA
                while (t.length() < 9) { // AÑADE AL DNI LOS 0 POR DELANTE
                    t = "0" + t;
                }
            }
            return t; // DEVUELVE EL DNI O EL NIE NORMALIZADO
        }
        return ""; // NO ES NI DNI NI NIE CORRECTO
    }
}
