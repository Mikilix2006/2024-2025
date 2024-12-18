package DNI-NIE-Validator.utilidades;
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Entrada {
        @SuppressWarnings("UseSpecificCatch")
	static String inicializar() {
		String buzon = "";
		InputStreamReader flujo = new InputStreamReader(System.in);
		BufferedReader teclado = new BufferedReader(flujo);
		try {
			buzon = teclado.readLine();
		} catch (Exception e) {
			System.out.append("Entrada incorrecta)");
		}
		return buzon;
	}

	public static int entero() {
		int valor = Integer.parseInt(inicializar());
		return valor;
	}

	public static double real() {
		double valor = Double.parseDouble(inicializar());
		return valor;
	}

	public static String cadena() {
		String valor = inicializar();
		return valor;
	}

	public static char caracter() {
		String valor = inicializar();
		return valor.charAt(0);
	}
}
