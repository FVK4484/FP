package fp.tipos.test;

import java.util.List;
import java.util.Set;

import fp.tipos.Persona;

public class EjercicioExpresiones {
	
	public static void main(String [] args) {
		
		Persona juan = new Persona("Juan", 20, true, 
								Set.of("fútbol", "cine"), 
								Set.of("España", "Chile"), 
								List.of("Don Quijote", "El Principito"));
		Persona maria = new Persona("Maria", 15, false, 
								Set.of("lectura", "música", "cine"), 
								Set.of("Francia", "Chile"), 
								List.of("El Principito", "1984"));
	    Persona pedro = new Persona("Pedro", 17, true, 
	    					Set.of ("fútbol", "natación"), 
	    					Set.of("México"), 
	    					List.of("Cien Años de Soledad", "Moby Dick", "1984"));
	    
	    	Boolean res=null;
	    	
	    	System.out.println("Juan tiene más de 18 años:");
	    	//TODO Sustituye null por la expresión adecuada
	    	res=null;
	    	System.out.println(res);
	    	
	    	System.out.println("Maria tiene licencia de conducir:");
	    	//TODO Sustituye null por la expresión adecuada
	    	res=null;
	    	System.out.println(res);

	    	System.out.println("Juan ha visitado Chile:");
	    	//TODO Sustituye null por la expresión adecuada
	    	res=null;
	    	System.out.println(res);

	    	System.out.println("A María le gustan el cine y la música:");
	    	//TODO Sustituye null por la expresión adecuada
	    	res=null;
	    	System.out.println(res);

	    	System.out.println("'El Principito' es el último libro que ha leído Maria:");
	    	//TODO Sustituye null por la expresión adecuada
	    	res=null;
	    	System.out.println(res);

	    	System.out.println("Ni Juan ni Pedro tienen licencia de conducir:");
	    	//TODO Sustituye null por la expresión adecuada
	    	res=null;
	    	System.out.println(res);

	    	System.out.println("Maria ha leído al menos 2 libros:");
	    	//TODO Sustituye null por la expresión adecuada
	    	res=null;
	    	System.out.println(res);

	    	System.out.println("María no ha visitado México, pero Pedro sí:");
	    	//TODO Sustituye null por la expresión adecuada
	    	res=null;
	    	System.out.println(res);

	    	System.out.println("Juan ha leído más libros que María pero menos que Pedro:");
	    	//TODO Sustituye null por la expresión adecuada
	    	res=null;
	    	System.out.println(res);

	    	System.out.println("Pedro no ha visitado Chile y tampoco le gusta el cine:");
	    	//TODO Sustituye null por la expresión adecuada
	    	res=null;
	    	System.out.println(res);

	    	System.out.println("El último libro que María ha leído es '1984' y Juan no lo ha leído aún:");
	    	//TODO Sustituye null por la expresión adecuada
	    	res=null;
	    	System.out.println(res);

	    	System.out.println("Pedro ha visitado más países que Juan o ha leído más libros que María:");
	    	//TODO Sustituye null por la expresión adecuada
	    	res=null;
	    	System.out.println(res);

	    	System.out.println("María tiene licencia de conducir o ha leído 'Moby Dick', pero no ambas cosas");
	    	//TODO Sustituye null por la expresión adecuada
	    	res=null;
	    	System.out.println(res);

	    	System.out.println("Juan ha visitado España o Francia, pero no ambos");
	    	//TODO Sustituye null por la expresión adecuada
	    	res=null;
	    	System.out.println(res);

	}

}
