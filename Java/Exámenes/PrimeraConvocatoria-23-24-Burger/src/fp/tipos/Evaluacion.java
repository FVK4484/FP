package fp.tipos;

import fp.utiles.Checkers;

public record Evaluacion(String hamburgueseria, int presentacion, int punto_carne
		, int calidad_ingredientes, int calidad_pan) {
	
	public Evaluacion {
		Checkers.check("El valor de valoración del punto de la carne debe estar "
					+ "comprendido entre 0 y 10.", presentacion>=0 && presentacion<=10);
		Checkers.check("El valor de valoración del punto de la carne debe estar "
				+ "comprendido entre 0 y 10.", punto_carne>=0 && punto_carne<=10);
		Checkers.check("El valor de valoración del punto de la carne debe estar "
				+ "comprendido entre 0 y 10.", punto_carne>=0 && punto_carne<=10);
		Checkers.check("El valor de valoración del punto de la carne debe estar "
				+ "comprendido entre 0 y 10.", punto_carne>=0 && punto_carne<=10);
	}
	
//	public void valor_presentacion() {
//		if(presentacion<=0 && presentacion>=10) {
//			throw new IllegalArgumentException("El valor de valoración de la presentación debe estar "
//					+ "comprendido entre 0 y 10.");
//		}
//	}
//	
//	public void valor_puntoCarne() {
//		if(punto_carne<=0 && punto_carne>=10) {
//			throw new IllegalArgumentException("El valor de valoración del punto de la carne debe estar "
//					+ "comprendido entre 0 y 10.");
//		}
//	}
//	
//	public void valor_calidadIngredientes() {
//		if(calidad_ingredientes<=0 && calidad_ingredientes>=10) {
//			throw new IllegalArgumentException("El valor de valoración de la calidad de los ingredientes debe estar "
//					+ "comprendido entre 0 y 10.");
//		}
//	}
//	
//	public void valor_calidadPan() {
//		if(calidad_pan<=0 && calidad_pan>=10) {
//			throw new IllegalArgumentException("El valor de valoración de la calidad del pan debe estar "
//					+ "comprendido entre 0 y 10.");
//		}
//	}
	
	public Double puntuacion_final() {
		return (presentacion + punto_carne + calidad_ingredientes + calidad_pan) / 4.0;
		}
}